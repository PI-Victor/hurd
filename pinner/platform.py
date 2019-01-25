from . import util

class VersionStack:
    def __init__(self):
        pass

    def search_version(self):
        pass

    def _walk_dir_tree(self):
        pass

class Platform:
    """Platform holds the general information about the platform config"""

    def __init__(self, version):
        self.version = version
        self.config_path = '{}/{}'.format(util.get_working_dir(), "config.yaml")

    def load_microservices():
        pass

    def load_config():
        try:
            print(this.config_path)
            # with open(this.config_path, encoding='utf-8') as fh.read():
            #     yaml = yaml.safe_load(fh)

        except OSError as e:
            raise e

        except yaml.YAMLError as e:
            raise e

class MicroService:
    """MicroService holds the microservice config and relevant functionality"""

    def __init__(self, alias, location, refs):
        self.alias = alias
        self.location = location
        self.refs = refs
