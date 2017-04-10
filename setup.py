from setuptools import setup

setup(name='python_package',
      version='0.0.1',
      description='Python package template',
      # see: https://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.5'
      ],
      url='http://github.com/storborg/funniest',
      author='Author',
      author_email='package_author@example.com',
      license='MIT',
      packages=['python_package'],
      # $ pip install -e .[dev,test]
      extras_require={
        'dev': [],
        'test': ['pytest'],
      },
      install_requires=[],
      zip_safe=False)


