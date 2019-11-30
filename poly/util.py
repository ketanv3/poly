import os
import importlib.util

from .exception import PolyException


def get_workspace_dir():
    """
    This ensures that 'POLY_WORKSPACE' environment variable is defined and is valid.
    :return:
    """
    poly_workspace = os.getenv('POLY_WORKSPACE')
    if poly_workspace is None:
        raise PolyException(f"'{poly_workspace}' is not a valid workspace")

    return poly_workspace.rstrip('/')


def get_import_path(workspace, argv):
    """
    Walks down the workspace directory to find the right module to be imported.
    :param workspace:
    :param argv:
    :return:
    """
    cwd: str = workspace

    for depth, path in enumerate(argv[1:]):
        cwd = cwd + '/' + path

        if os.path.isdir(cwd):
            continue

        if not os.path.isfile(cwd + '.py'):
            raise PolyException(f"'{cwd + '.py'}' not found")

        return cwd, depth + 2

    raise PolyException(f"'{cwd}' is not the leaf")


def load_module(import_path):
    """
    Loads the module from the given import path.
    Also ensures the 'command' function is present in the module.
    :param import_path:
    :return:
    """
    spec = importlib.util.spec_from_file_location(import_path, import_path + '.py')
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)

    if not hasattr(module, 'command') or not callable(module.command):
        raise PolyException(f"'command' is not callable in '{import_path}'")

    return module
