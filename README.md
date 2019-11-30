# poly <img src="./docs/poly.svg" width="80" align="right" />

Manage all your command line tools easily in one place!


## Installation

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
python -m pytest --cov=flux --cov-report term-missing
```

## Issues and Suggestions
If you encounter any issues or have suggestions, please [file an issue](https://github.com/ketanv3/poly/issues) along with a detailed description. Remember to apply labels for easier tracking. 


## Versioning
We use [SemVer](http://semver.org/) for versioning. For the available versions, see the [tags on this repository](https://github.com/ketanv3/poly/tags)


## Authors
See the list of [contributors](https://github.com/ketanv3/poly/contributors) who participated in this project.
