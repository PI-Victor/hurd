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

class NoPlatformVersionDefined(Exception):
    """This exception is raised when there is no platform version defined in
    config.yaml.
    """
    pass

class NoPlatformNameDefined(Exception):
    """This exception is raised when there is no platform name defined in
    config.yaml.
    """
    pass

class ComponentUndefinedError(Exception):
    """This exception is raised whenever an alias does not have a mapping
    component defined in the config version file.
    """
    pass

class ComponentTagUndefinedError(Exception):
    """This exception is raised whenever a tag is undefined on a component
    """
    pass

class ComponentRefsUndefinedError(Exception):
    """This exception is raised whenever a ref is undefined on a component
    """
    pass

class SemverNonCompliantError(Exception):
    """This exception is raised whenever the requested version does not 
    comply with semantic versioning.
    """
    pass


class MultiplePlatformVersionsFound(Exception):
    """This exception is raised whenever the version passed by the user 
    is too broad and returns multiple results.
    By definition you cannot fetch mutiple versions of a component.
    """
    pass
