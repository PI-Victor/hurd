import os, re
from fnmatch import filter as fnfilter


def open_file(config_file):
    try:
        with open(config_file) as cf:
            return cf.read()

    except OsError as osError:
        # NOTE: wrap it!?
        raise osError

    except IOError as ioError:
        raise ioError

def get_platform_versions(workspace_path, version=''):
    """Walks the specified directory where the platform versioning is located
    and will try to find all the directories that match a regex of v[0-9]+.
    e.g.: v1, v2, v2.2 return:
    :param workspace_path: string
    :param version: string
    :return: returns a list of strings that contains the full path that match
    the regex.
    """
    _regex = re.compile(version)
    version_dir = list(
        filter(lambda s: _regex.match(s), os.listdir(workspace_path))
    )
    # NOTE: any way to ditch [0]?
    version_path = os.path.join(workspace_path, version_dir[0])
    return fnfilter(os.listdir(version_path), '*.yaml')
