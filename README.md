# Minimal python package development example

Minimal package development example project. Only defines a class with dummy functionality and some demo tests. Minimal package project structure. Best practices for package development in python.

## TODO

* create account at pypi.python.org and add .pypirc file
* git tag and release on github
* publish the package

## Project structure

| File or folder  | Description  |
|---|---|
| setup.py  | Module configuration.  |
| setup.cfg  | PyPi configuration.  |
| README.md  | this file.  |
| python_package_quickstart/  | The actual package/module. Where all the code resides.  |
| tests/  | Sample unit test using py.test.  |


## Development

To develop a module based on this project follow this instructions.

### Create a virtualenv for development packages

It's allways a good idea to create an enviroment for the module.

```bash
conda create --name packages_p3 python=3.5
source activate packages_p3
conda install virtualenv
virtualenv venv
```

## Installing dev and test dependencies
```bash
pip install -e .[dev,test]
```

## ​Working in “Development Mode”

While you are developing the module you can install your module from source:

```bash
pip install -e .
python3 
```

And you can import the module and testing in python.

```bash
$ ▶ python3
Python 3.5.3 |Continuum Analytics, Inc.| (default, Mar  6 2017, 11:58:13)
[GCC 4.4.7 20120313 (Red Hat 4.4.7-1)] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import python_package
>>> type(ob)
<class 'python_package.example.Example'>
>>> ob.hello()
'Hello!!'
```

## Test and coverage

To run the test:

```bash
$ py.test tests
==================================== test session starts =====================================
...
collected 4 items

tests/test_hello.py ...s

============================ 3 passed, 1 skipped in 0.02 seconds =============================
```

To run the coverage:

```bash
$ py.test --cov=python_package_quickstart tests/

 ==================================== test session starts =====================================
 ...
tests/test_hello.py ...s
----------- coverage: platform linux, python 3.5.3-final-0 -----------
Name                         Stmts   Miss  Cover
------------------------------------------------
python_package_quickstart/__init__.py       1      0   100%
python_package_quickstart/example.py        5      0   100%
------------------------------------------------
TOTAL                            6      0   100%

============================ 3 passed, 1 skipped in 0.05 seconds =============================
```

## Generate documention

To generate documentation:

```bash
cd docs
make html
```

The index.html is generated based on docs/index.rst. A simple file of how to autogenerate documentation from the docstring on your code can be found in docs/code.rst, this use autocode. for more infomation you can read:

* [Sphinx](http://www.sphinx-doc.org/en/stable/tutorial.html) 

* [Autodoc](http://www.sphinx-doc.org/en/stable/ext/autodoc.html)


# Publish your package on PyPi hosting on github

PyPi is a package index for python, it is what you use when you install a package using pip. If you don't have already, create accounts at 
[PyPI Live](https://pypi.python.org/pypi?%3Aaction=register_form) and [PyPI Test](https://testpypi.python.org/pypi?%3Aaction=register_form).

## Create a .pypirc configuration file

Create a file called .pypirc with the following configuration from your PyPi accounts:

```bash
[distutils]
index-servers =
  pypi
  pypitest

[pypi]
repository: https://pypi.python.org/pypi
username: <username>
password: <password>

[pypitest]
repository: https://test.pypi.org/legacy/
username: <username>
password: <password>
```

I don't use the password field, you can remove it if you don't mind to enter your password whenever you publish a package.

## Checklist for publishing

- [] Update changelog.txt
- [] Update version number in setup.py
- [] Update version number in documentation
- [] Convert README.md to README.rst (using pandoc)
pandoc --columns=100 --output=README.rst --to rst README.md
- [] Add tarball download url to setup.py. 
```python
setup(
    ...
    url = 'https://github.com/gabrielrezzonico/python_package',
    download_url = 'https://github.com/sheriferson/python_package/tarball/0.1.0',
    ...
```
Even if it doesn't exists yet in github
- [] Update HISTORY.rst and MANIFEST.in
A simple way to do it is with this command:
```bash
git log --pretty=oneline --abbrev-commit | grep 'feat\|fix' > HISTORY.rst
```
Not the best option.
- [] Commit everything
- [] Create tag with the version number
- [] Push to github, use the --tags flags to push the tag too.
- [] Create a source distribution
```bash
python setup.py sdist bdist_wheel
```
- [] Test the package in PyPi Test:
```bash
twine upload --repository pypitest dist/*
```
- [] Install the package from PyPi Test:
```bash
pip install -i https://testpypi.python.org/pypi python_package_quickstart
```
- [] Publish the package to PyPi Live:
```bash
twine upload dist/*
```
- [] Install the package using pip:
```bash
pip install python_package_quickstart
```