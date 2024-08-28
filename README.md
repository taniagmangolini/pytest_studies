Studies related to the book 'Testing with pytest', Brian Okken, Oreally.

Book git: https://github.com/jashburn8020/python-testing-with-pytest/tree/master

# Set a nice theme

```
Install extension Dracula.
```

# IDE settings

## AUTOPEP8

CTRL+P run command:

```
ext install ms-python.autopep8
```

To format a document: CTRL+P and run 'Format Document'.
It is possible on File/Preferences to set an option to Format On Save.

# Virtual env

```
python3 -m venv .venv
```

# Error checking

Install extension Flake8.
Run:

```
flake8 src
```

# Packaging

The build process installs the setuptools and wheel packages.
It should be named pyproject.toml or setup.py.

## Build

```
pip install -q build
python -m build
```

## Install

```
python -m pip install dist/python_packaging-0.0.1-py3-none-any.whl
```

## Run

```
python-packaging
```

# Tests

```
pip install pytest
```

## Mock and Coverage

```
pip install pytest-mock

pip install pytest-cov
```

## Debug test errors

```
pytest --pdb
```

## Coverage

```
pytest --cov=src
```
