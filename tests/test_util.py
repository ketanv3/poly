import os
import pytest

import poly
import poly.util


def test_workspace_dir():
    # Check if an exception is raised when the workspace environment variable is not set.
    os.environ.pop('POLY_WORKSPACE', None)
    with pytest.raises(poly.PolyException) as e:
        poly.util.get_workspace_dir()
    assert e.value.reason.startswith('POLY_WORKSPACE is not configured')

    # Exception should be raised when the directory is invalid.
    invalid_workspace = os.path.dirname(__file__) + '/some/invalid/path'
    os.environ['POLY_WORKSPACE'] = invalid_workspace
    with pytest.raises(poly.PolyException) as e:
        poly.util.get_workspace_dir()
    assert e.value.reason.endswith('is not a valid workspace')

    valid_workspace = os.path.dirname(__file__) + '/test_workspace/'
    os.environ['POLY_WORKSPACE'] = valid_workspace
    assert valid_workspace.rstrip('/') == poly.util.get_workspace_dir()


def test_import_path():
    mock_workspace = os.path.dirname(__file__) + '/test_workspace'

    # Should fail with 'invalid command path' as 'baz' is not a valid command in '.../foo/'
    mock_argv = ['poly', 'foo', 'baz']
    with pytest.raises(poly.PolyException) as e:
        poly.util.get_import_path(mock_workspace, mock_argv)
    assert e.value.reason.startswith('invalid command path')

    # Should fail with 'no leaf command yet' as '.../foo/' is a directory.
    mock_argv = ['poly', 'foo']
    with pytest.raises(poly.PolyException) as e:
        poly.util.get_import_path(mock_workspace, mock_argv)
    assert e.value.reason.startswith('no leaf command yet')

    mock_argv = ['poly', 'foo', 'bar']
    path, depth = poly.util.get_import_path(mock_workspace, mock_argv)
    assert path == mock_workspace + '/foo/bar'
    assert depth == 3


def test_load_module():
    mock_workspace = os.path.dirname(__file__) + '/test_workspace'

    mock_argv = ['poly', 'foo', 'bad']
    path, depth = poly.util.get_import_path(mock_workspace, mock_argv)
    with pytest.raises(poly.PolyException) as e:
        poly.util.load_module(path)
    assert e.value.reason.startswith("'command' is not callable in")

    # This should work.
    mock_argv = ['poly', 'foo', 'bar']
    path, depth = poly.util.get_import_path(mock_workspace, mock_argv)
    poly.util.load_module(path)
