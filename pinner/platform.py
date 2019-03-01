from threading import Thread
from typing import List
from os import path, environ

from pygit2 import clone_repository, Keypair, RemoteCallbacks

from . import util
from . import errors


class Platform:
    """Platform holds the general metadata and functionality about the platform
    config.
    """
    threads: List[Thread]
    name: str = None
    version: str = None
    components: List = []

    def __init__(self, workspace) -> None:
        self._components = []
        self._threads = []

        config_file = path.join(workspace, 'config.yaml')
        config = util.open_file(config_file)

        self.parse_config(config)

    def parse_config(self, config) -> None:
        for data in config:
            self.name = data.get('name')
            if not self.name:
                raise errors.NoPlatformNameDefined('No platform name defined in config.yaml')

            for key, value in data.items():
                if key == 'name':
                    self.name = value
                    continue

                if key == 'components':
                    for component in value:
                        self._components.append(
                            MicroService(
                                alias=component.get('alias'),
                                location=component.get('url'),
                            )
                        )

    def __repr__(self) -> str:
        return self.version

    def __eq__(self, version) -> bool:
        return self.version == version

    def update_components(self, vers_config) -> None:
        self.version = vers_config.get('version')
        if not self.version:
            raise errors.NoVersionFoundError('No platform version was defined in config file')

        vers_components = vers_config.get('components')
        if not vers_components:
            raise errors.NoComponentsDefinedError(f'No components are defined for {self.version}')

        for component in self._components:
            match = next((c for c in vers_components if c.get('alias') == component), None)
            if not match:
                raise errors.ComponentUndefinedError(f"Component '{component['name']}' does not have a defined alias in config.yaml")

            component.refs = match.get('refs')
            if not component.refs:
                raise errors.ComponentTagUndefinedError()

            component.hash = match.get('hash')
            if not component.hash:
                raise errors.ComponentRefsUndefinedError()

    async def fetch_components(self, repo_path, user, ssh_private_key, ssh_pub_key) -> None:
        workspace = path.join(repo_path, self.name)

        for component in self._components:
            print(component)
            await component.fetch(
                workspace, user, ssh_pub_key, ssh_private_key,
            )


class MicroService:
    """MicroService holds the microservice config and relevant functionality"""    
    refs: str = None
    hash: str = None

    
    def __init__(self, alias, location) -> None:
        self.alias = alias
        self.location = location

    def __repr__(self) -> str:
        return self.alias

    def __eq__(self, alias) -> bool:
        return self.alias == alias

    async def fetch(self, workspace, user, ssh_pub_key, ssh_private_key, validate=False) -> None:
        """This function will try to create the workspace for the component that
        will be cloned, will fetch the component and will export the environment 
        variable that points to component cloned repository.
        """
        await self._clone(workspace, user, ssh_pub_key, ssh_private_key)
        if validate:
            await self._export_env(workspace)

    async def _clone(self, workspace, user, ssh_pub_key, ssh_private_key) -> None:
        ws = util.create_workspace(workspace, self.alias)
        print(f'{user}, {ssh_private_key}, {ssh_pub_key}')
        keypair = Keypair(
            username=user,
            pubkey=ssh_pub_key,
            privkey=ssh_private_key,
            passphrase='',
        )
        
        try:
            clone_repository(
                url=self.location,
                path=ws,
                checkout_branch='master',
                callbacks=RemoteCallbacks(
                    credentials=keypair,
                ),
            )
        except Exception as e:
            # TODO: make this more relevant.
            raise e

    async def _export_env(self, workspace) -> None:
        """Used to export the path of the cloned git repository.
        Useful in CI/CD platform pipelines.
        """
        _name = f'{self.alias}_WORKSPACE'.upper()
        environ[_name] = workspace
