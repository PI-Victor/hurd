from os import path

from . import util
from .errors import NoVersionFoundError, NoComponentsDefinedError, \
    ComponentUndefinedError


class Platform:
    """Platform holds the general metadata and functionality about the platform
    config
    """
    def __init__(self, workspace, version=''):
        self.version = version
        self._components = []

        config_file = path.join(workspace, "config.yaml")
        config = util.open_file(config_file)

        for component in next(data.get('components') for data in config):
            self._components.append(
                MicroService(
                    alias=component.get('name'),
                    location=component.get('url'),
                )
            )

    def __repr__(self):
        return self.version

    def __eq__(self, version):
        return self.version == version

    def update_components(self, vers_config):
        self.version = vers_config.get('version')

        if self.version is None:
            raise NoVersionFoundError('No platform version was defined in file')

        components = vers_config.get('components')

        if components is None:
            raise NoComponentsDefinedError(f'No components are defined for {version}')

        for component in components:
            name = component.get('name')

            if not (name in self._components):
                raise ComponentUndefinedError(f"Component '{component['name']}' does not have a defined alias in config.yaml")


class MicroService:
    """MicroService holds the microservice config and relevant functionality"""

    def __init__(self, alias, location, tags='', refs=''):
        self.alias = alias
        self.location = location
        self.tag = ''
        self.refs = ''

    def __repr__(self):
        return f'{self.alias}:{self.refs}:{self.tag}'

    def __eq__(self, alias):
        return self.alias == alias

    def _clone(self):
        pass

    def _export_environment(self):
        pass
