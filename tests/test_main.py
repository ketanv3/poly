import os
import sys
import poly
import pytest


def test_main():
    # Tests everything end-to-end.
    os.environ['POLY_WORKSPACE'] = os.path.dirname(__file__) + '/test_workspace/'
    sys.argv = ['poly', 'foo', 'bar', '--name', 'poly', '--count', '5']
    with pytest.raises(SystemExit) as e:
        poly.main()
    assert e.value.code == 0
