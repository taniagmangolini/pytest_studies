Studies related to the book 'Testing with pytest', Brian Okken, Oreally.

Book git: https://github.com/jashburn8020/python-testing-with-pytest/tree/master

# NICE THEME

```
Install extension Dracula.
```

# VSCODE FORMATTING

## AUTOPEP8

CTRL+P run command:

```
ext install ms-python.autopep8
```

To format a document: CTRL+P and run 'Format Document'.
It is possible on File/Preferences to set an option to Format On Save.

# CREATE VIRTUAL ENV

```
python3 -m venv .venv
```

# ERROR CHECKING

Install extension Flake8.
Run:

```
flake8 src
```

# PACKAGING

## CREATE .TOML FILE

Notice that the build process installs the setuptools and wheel pack-
ages.
It should be named pyproject.toml or setup.py.

## BUILD

```
pip install -q build
python -m build
```

## INSTALL

```
python -m pip install dist/python_packaging-0.0.1-py3-none-any.whl
```

## RUN

```
python-packaging
```

# TEST

```
pip install pytest
```

## MOCK

```
pip install pytest-mock
```

## DEBUG ERROR

```
pytest --pdb
```

## COVERAGE

```
pytest --cov=src
```
