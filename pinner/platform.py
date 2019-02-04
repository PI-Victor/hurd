from . import util


class Platform:
    """Platform holds the general metadata and functionality about the platform
    config"""

    def __init__(self, version, workspace):
        self.version = version
        self.config_path = os.path.join(workspace, 'config.yaml')

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
