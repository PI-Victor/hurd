import os, re

import click

from pinner import platform
from pinner.util import get_working_dir


def validate_version(ctx, param, value):
    """Custom validation for --version option"""
    if param.name == 'version' and not value:
        raise click.BadParameter('you need to pass a platform version')

def validate_workspace(ctx, param, value):
    """Custom validation for --workspace option"""
    if param.name == 'workspace' and not value:
        if not ('PINNER_WORKSPACE' in os.environ) or os.environ.get('PINNER_WORKSPACE') == '':
            raise click.UsageError("""missing --workspace or export PINNER_WORKSPACE
pointing to the full path --directory where the config and platform versioning
are located.""")

_global_options = [
    click.option(
        '--version',
        help='The specific platform version',
        callback=validate_version,
    ),
    click.option(
        '--workspace',
        envvar='PINNER_WORKSPACE',
        help="""The workspace containing the configuration and the platform
        versioning in yaml format.""",
        callback=validate_workspace,
        type=click.Path(),
    ),
]

def add_option(options):
    """Wraps a defined function with global parameters"""
    def _add_options(func):
        for option in reversed(options):
            func = option(func)
        return func
    return _add_options

def new_platform(version, **kwargs):
    return platform.Platform(version, **kwargs)

def get_platform_versions(workspace_path):
    """Will walk the current directory where the application is located and will
    try to find all the directories that match a regex of v[0-9]+. e.g.: v1, v2,
    v2.2 return: a list of strings that contain the directory names that match
    the regex."""
    _regex = re.compile("v[0-9]+")

    return list(filter(lambda s: _regex.match(s), os.listdir(workspace_path)))

def search_version(major_versions, version):
    """Searches for a specified version in the major versions"""
    pass

@click.group()
def cli():
    pass

@cli.command(
    help="""This command will start fetching all the repositories defined in a
    pinned version that match the specific version found. If multiple pinned
    versions match, it will fail with an error."""
)
@add_option(_global_options)
def fetch(version, workspace):
    pass

@cli.command(
    help="""Displays the pinned microservice versions together with some
    relevant metadata such as pinned refs and url. The data is tabulated."""
)
@add_option(_global_options)
def describe(version, workspace):
    major_version = get_platform_versions(workspace)

@cli.command(
    help="""This command will validate the defined platform pinned version by
    trying to fetch the refs described. If multiple versions match, it will try
    to validate all of them."""
)
@add_option(_global_options)
def validate(version, workspace):
    pass

if __name__ == '__main__':
    cli()
