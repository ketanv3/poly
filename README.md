# poly <img src="./docs/poly.svg" width="80" align="right" />

[![Python Version](https://img.shields.io/badge/python-3.7-blue.svg)](https://www.python.org/downloads/release/python-370/)
[![Coverage](./docs/coverage.svg)]()
[![Maintainability](https://api.codeclimate.com/v1/badges/7dcde6b92ad3bc7db5ac/maintainability)](https://codeclimate.com/github/ketanv3/poly/maintainability)

Manage all your command line tools easily in one place!


## Quick Start Guide

#### Easy Install

Poly can be installed easily with the following command:

```bash
curl https://raw.githubusercontent.com/ketanv3/poly/master/scripts/install.sh -o install-poly.sh && chmod 755 ./install-poly.sh && ./install-poly.sh
```

Depending on your configuration, you might need to run this command with `sudo`. If this fails for you, follow the manual install procedure given below.

#### Workspace

`POLY_WORKSPACE` environment variable defines the root directory that containing all your executable commands. Add it to `.bashrc` / `.zshrc` or similar so that it's sourced every time a new shell is launched.

```bash
export POLY_WORKSPACE=~/poly_ws/
```

A workspace contains bunch of folders and files (leaf nodes) which form the searchable command path.
```
↳ poly_ws
   ↳ foo
      ↳ bar
         ↳ hello_world.py
   ↳ code
      ↳ vscode.py
      ↳ intellij.py
   ↳ base64
      ↳ encode.py
      ↳ decode.py
```

#### Creating Commands

Creating these commands is pretty easy in itself. We use [Click](https://click.palletsprojects.com/en/master/python3/) library to generate command line utilities.

Here's a simple `hello-world.py` example:

```python
import click

@click.command()
@click.option('--name', required=True)
@click.option('--count', default=1)
def command(name, count):
    for i in range(count):
        print(f'Hello, {name}!')
```

#### Executing Commands

To execute the above command:
```bash
poly foo bar hello_world --name poly --count 5
```



## Manual Installation

Make sure you're running Python 3.6+. Run the following command to confirm.
```bash
python --version
```

Once Python version is confirmed, clone the project and run the following commands from the root directory of the project:
```bash
python setup.py install
```

That's it! Poly should now be installed! Confirm by running the following command:
```bash
poly
```


## Running Tests

To build the module and run the tests, run the following command:

```bash
python setup.py test
```

Alternatively, tests can be run without building the module. To also report the code coverage, use the following command:

```bash
python -m pytest --cov=poly --cov-report term-missing
```

## Issues and Suggestions
If you encounter any issues or have suggestions, please [file an issue](https://github.com/ketanv3/poly/issues) along with a detailed description. Remember to apply labels for easier tracking. 


## Versioning
We use [SemVer](http://semver.org/) for versioning. For the available versions, see the [tags on this repository](https://github.com/ketanv3/poly/tags)


## Authors
See the list of [contributors](https://github.com/ketanv3/poly/contributors) who participated in this project.
