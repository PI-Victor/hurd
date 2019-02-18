from os import path

from . import util
from . import errors


class Platform:
    """Platform holds the general metadata and functionality about the platform
    config
    """
    def __init__(self, workspace):
        self.name = ''
        self.version = ''
        self._components = []

        config_file = path.join(workspace, "config.yaml")
        config = util.open_file(config_file)

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

        if not self.version:
            raise errors.NoVersionFoundError('No platform version was defined in config file')

        vers_components = vers_config.get('components')

        if not vers_components:
            raise errors.NoComponentsDefinedError(f'No components are defined for {self.version}')

        for component in self._components:
            match = next((c for c in vers_components if c.get('name') == component), None)

            if not match:
                raise errors.ComponentUndefinedError(f"Component '{component['name']}' does not have a defined alias in config.yaml")

            component.refs = match.get('refs')

            if not component.refs:
                raise errors.ComponentTagUndefinedError()

            component.hash = match.get('hash')

            if not component.hash:
                raise errors.ComponentRefsUndefinedError()


class MicroService:
    """MicroService holds the microservice config and relevant functionality"""

    def __init__(self, alias, location):
        self.alias = alias
        self.location = location
        self.refs = ''
        self.hash = ''

    def __repr__(self):
        return self.alias

    def __eq__(self, alias):
        return self.alias == alias

    def _clone(self):
        pass

    def _export_environment(self):
        pass
