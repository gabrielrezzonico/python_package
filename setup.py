from setuptools import setup

setup(name='python_package',
      version='0.1',
      description='Minimal python package development example',
      # see: https://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
          'Development Status :: 3 - Alpha',
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python :: 3.5'
      ],
      url='https://github.com/gabrielrezzonico/python_package_example',
      author='Author',
      author_email='package_author@example.com',
      license='MIT',
      packages=['python_package_example'],
      # $ pip install -e .[dev,test]
      extras_require={
          'dev': ['sphinx'],
          'test': ['pytest', 'pytest-cov'],
      },
      install_requires=[],
      zip_safe=False)


