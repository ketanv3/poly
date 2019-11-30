#!/usr/bin/env python3

"""
Poly allows you to manage all your command line tools easily in one place.
"""

import sys
import poly


if __name__ == '__main__':
    try:
        poly.main()
    except poly.PolyException as e:
        print(e.reason, file=sys.stderr)
        exit(1)
