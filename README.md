[![.github/workflows/test](https://github.com/SamuelHomberg/packaging_tutorial/actions/workflows/test.yml/badge.svg)](https://github.com/SamuelHomberg/packaging_tutorial/actions/workflows/test.yml)
[![Documentation Status](https://readthedocs.org/projects/example-package-samuelhomberg/badge/?version=latest)](https://example-package-samuelhomberg.readthedocs.io/en/latest/?badge=latest)


# A project to teach myself how to publish python packages

Using the following tools:
- Testing: [pytest](https://docs.pytest.org/en/8.0.x/index.html)
- Building: [flit](https://flit.pypa.io/en/stable/)
- Documentation: [sphinx](https://www.sphinx-doc.org/en/master/index.html), [readthedocs](https://about.readthedocs.com/)
- Publishing: [TestPyPi](https://test.pypi.org/), Github Actions

Inspired by projects from [Marvin Friede](https://github.com/marvinfriede/template-python-project) and [Martin Buttenschoen](https://github.com/maabuu/posebusters/).

## Configuration

The most important configuration options for everything are found in the [pyproject.toml](pyproject.toml)-file.

## Example code and tests

Following convention, the code for the package **example_package_samuelhomberg** lives at [src/example_package_samuelhomberg/](src/example_package_samuelhomberg) and the corresponding tests at [test/](test).
Whyle pytest is used for testing, the actual tests are written using the unittest package. The code and tests are of no further importance.

## Documentation

The documentation is configured (path to code, theme, logo and favicon, ...) in [docs/source/conf.py](docs/source/conf.py).

Documentation was written using [sphinx](https://www.sphinx-doc.org/en/master/index.html) and the project the registered at [readthedocs](https://about.readthedocs.com/) for automatically updating documentation.

## Building and manual publishing

I followed [this guide](https://packaging.python.org/en/latest/tutorials/packaging-projects/) to build a package and manually uploaded it to PyPi (or in this case, only to TestPyPi).
The building backend [flit](https://flit.pypa.io/en/stable/) relies on the configuration in [pyproject.toml](pyproject.toml) and can dynamically load the version number and short project description.

## Automated Testing, Publishing and Releasing

The workflows configuring the github actions are found in [.github/workflows/](.github/workflows/).

### Automated Testing

This is done using the [test.yml](.github/workflows/test.yml) workflow.
As of now, the tests are not really automated but manually triggered (see [Future Improvements](#future-improvements)). 

### Automated Building, Publishing and Releasing

This is done using the [publish_release.yml](.github/workflows/publish_release.yml) workflow, which is heavily based on the [guide found here](https://packaging.python.org/en/latest/guides/publishing-package-distribution-releases-using-github-actions-ci-cd-workflows/).
This workflow is also manually triggered. To still have version numbers for the GitHub Release, [get_version.py](get_version.py) script saves a file with the version, which can is used in the workflow.
As before, it would be better to switch to a tagged release scheme (see [Future Improvements](#future-improvements)). 

## Future Improvements

- **Instead of using manually controlled workflows (`workflow_dispatch`), it would be better to have a complete [build -> test -> publish -> release] workflow tied to [tagged commits](https://git-scm.com/book/en/v2/Git-Basics-Tagging), as in [this example](https://packaging.python.org/en/latest/guides/publishing-package-distribution-releases-using-github-actions-ci-cd-workflows/) using `${{ github.ref_name }}`.** However, automatic releases apparently create tags with version numbers.
---
- Linting with [ruff](https://github.com/astral-sh/ruff)
- [codecov](https://about.codecov.io/)
- ...
- (more fancy badges?)