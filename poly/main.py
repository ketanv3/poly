import sys

from .util import (
    get_workspace_dir,
    get_import_path,
    load_module
)


def main():
    # Walk down the workspace directory to locate the correct module to be imported.
    workspace = get_workspace_dir()
    import_path, depth = get_import_path(workspace, sys.argv)
    module = load_module(import_path)

    # Updating sys.argv so the help menu shows the full correct command.
    sys.argv = [' '.join(sys.argv[:depth])] + sys.argv[depth:]

    # Run the command!
    module.command()
