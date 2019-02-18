import click

from pinner import util
from pinner.platform import Platform
from pinner.errors import NoVersionFoundError

def validate_version(ctx, param, value):
    """Custom validation for --version option"""
    if param.name == 'version' and not value:
        raise click.BadParameter('you need to pass a platform version')
    return value

def validate_workspace(ctx, param, value):
    """Custom validation for --workspace option"""
    if param.name == 'workspace' and not value:
        if not ('PINNER_WORKSPACE' in os.environ) or os.environ.get('PINNER_WORKSPACE') == '':
            raise click.UsageError("""pass --workspace or export
            PINNER_WORKSPACE pointing to the full path directory where the
            YAML platform version is located.
            """
            )
    return value

def validate_path(ctx, param, value):
    pass

_global_options = [
    click.option(
        '--version',
        '-v',
        help='The specific platform version',
        callback=validate_version,
    ),
    click.option(
        '--workspace',
        '-w',
        envvar='PINNER_WORKSPACE',
        help="""The fullpath to the workspace containing the configuration and
        the platform versioning in yaml format.
        """,
        callback=validate_workspace,
        type=click.Path(exists=True),
    ),
]

def add_option(options):
    """Wraps a defined function with global parameters"""
    def _add_options(func):
        for option in reversed(options):
            func = option(func)
        return func
    return _add_options

@click.group()
def cli():
    pass

@cli.command(
    help="""This command will start fetching all the repositories defined in a
    pinned version that match the specific version found. If multiple pinned
    versions match, it will fail with an error.
    """
)
@add_option(_global_options)
def fetch(version, workspace):
    pass

@cli.command(
    help="""Displays tabulated metadata about the pinned microservice platform
    version.
    """
)
@add_option(_global_options)
def describe(version, workspace):
    platforms = util.filter_version(version, workspace)
    for version in [c for c in platforms]:
        for v in version._components:
            print(f'{version}:{v.hash}:{v.alias}:{v.location}')

@cli.command(
    help="""This command will validate the defined platform pinned version by
    trying to fetch the refs described. If multiple versions match, it will
    throw an exception.
    """
)
@add_option(_global_options)
def validate(version, workspace):
    pass

@cli.command(
    help="""This command will create a new git tag in the repositories defined
    by the YAML platform version config.
    Throws an exception if a a tag has been defined but does not match the one
    specified.
    """
)
@add_option(_global_options)
@click.option(
    '--path',
    help="""Full path to where the artifacts should be cloned.
    """,
    type=click.Path(),
    callback=validate_path,
    envvar='PINNER_ARTIFACTS',
)
def tag(version, workspace):
    pass

if __name__ == '__main__':
    cli()
