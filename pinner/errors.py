class NoVersionFoundError(Exception):
    """This exception is thrown when
    a) there is no directory found for a
    specific version in the specified workspace.
    b) there is YAML version file that matches the desired version.
    """
    pass

class NoComponentsDefinedError(Exception):
    """This exception is raised when there are no components defined under a
    platform.
    """
    pass

class ComponentUndefinedError(Exception):
    """This exception is raised whenever an alias does not have a mapping
    component defined in the config version file.
    """
    pass
