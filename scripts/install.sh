#!/usr/bin/env bash

command -v python3 || { echo 'python3 not installed'; exit 1; }
command -v pip || { echo 'pip not installed'; exit 1; }
command -v git || { echo 'git not installed'; exit 1; }

mkdir -p /tmp && cd /tmp
rm -rf /tmp/poly

git clone https://github.com/ketanv3/poly.git && cd poly
python setup.py install

rm -rf /tmp/poly

echo 'poly has been installed successfully!'
