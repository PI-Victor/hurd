import click

from pinner.util import get_config_paths


def validate_version(ctx, param, value):
    """Custom validation for --version option"""
    if param.name == 'version' and not value:
        raise click.BadParameter('you need to pass a platform version')
    return value

def validate_workspace(ctx, param, value):
    """Custom validation for --workspace option"""
    if param.name == 'workspace' and not value:
        if not ('PINNER_WORKSPACE' in os.environ) or os.environ.get('PINNER_WORKSPACE') == '':
            raise click.UsageError(
            """missing --workspace or export
            PINNER_WORKSPACE pointing to the full path directory where the
            config and platform versioning are located.
            """
            )
    return value

_global_options = [
    click.option(
        '--version',
        help='The specific platform version',
        callback=validate_version,
    ),
    click.option(
        '--workspace',
        envvar='PINNER_WORKSPACE',
        help="""
        The workspace containing the configuration and the platform
        versioning in yaml format.
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
    help="""
    This command will start fetching all the repositories defined in a
    pinned version that match the specific version found. If multiple pinned
    versions match, it will fail with an error.
    """
)
@add_option(_global_options)
def fetch(version, workspace):
    pass

@cli.command(
    help="""
    Displays the pinned microservice versions together with some
    relevant metadata such as pinned refs and url. The data is tabulated.
    """
)
@add_option(_global_options)
def describe(version, workspace):
    yaml_files = get_config_paths(workspace, version)
    print(yaml_files)

@cli.command(
    help="""
    This command will validate the defined platform pinned version by
    trying to fetch the refs described. If multiple versions match, it will try
    to validate all of them.
    """
)
@add_option(_global_options)
def validate(version, workspace):
    pass

if __name__ == '__main__':
    cli()
