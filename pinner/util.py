import os, re
from fnmatch import filter as fnfilter


class NoVersionFoundError(Exception):
    """This exception is thrown whenever there is no directory found for a
    specific version in the specified workspace.
    """
    pass

def open_file(config_file):
    try:
        with open(config_file) as cf:
            return cf.read()

    except OsError as osError:
        # NOTE: wrap it!?
        raise osError

    except IOError as ioError:
        raise ioError

def get_config_paths(workspace_path, version=''):
    """Walks the specified directory where the platform versioning is located
    and will try to find all the directories that match a regex of v[0-9]+.
    e.g.: v1, v2, v2 return:
    :param workspace_path: string path to the workspace where the configuration
    is located.
    :param version: string the specific version to search for.
    :return: a list of all yaml files present in the specified version directory.
    """
    _regex_version = re.compile("v[0-9]+")

    version_dir = next((path for path in os.listdir(workspace_path) if _regex_version.match(path)), None)

    if version_dir is None:
        raise NoVersionFoundError(f'No version directory for version: {version} was found in {workspace_path}')

    version_path = os.path.join(workspace_path, version_dir)
    versions = list(filter(lambda p: re.search(version, p), os.listdir(version_path)))

    if not versions:
        raise NoVersionFoundError(f'No version {version} has been defined in path {version_path}')

    return list(map(lambda p: os.path.join(version_path, p), versions))
