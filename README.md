# Minimal package/module sample

Minimal python module/package sample project. Only defines a class with dummy functionality and some demo tests. Minimal project structure.

## TODO

* add test coverage
* generate documentation using Sphinx
* create account at pypi.python.org and add .pypirc file
* git tag and release on github
* publish the package

## Project structure

| File or folder  | Description  |
|---|---|
| setup.py  | Module configuration.  |
| setup.cfg  | PyPi configuration.  |
| README.md  | this file.  |
| python_package/  | The actual package/module. Where all the code resides.  |
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