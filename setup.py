#!/usr/bin/env python

import pip
from pip.req import parse_requirements
import os
import sys

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()

readme = open('README.rst').read()
doclink = """
Documentation
-------------

The full documentation is at http://my_checker.rtfd.org."""
history = open('HISTORY.rst').read().replace('.. :changelog:', '')

parsed_requirements = parse_requirements(
    'requirements/prod.txt',
    session=pip.download.PipSession()
)

parsed_test_requirements = parse_requirements(
    'requirements/dev.txt',
    session=pip.download.PipSession()
)

requirements = [str(ir.req) for ir in parsed_requirements]
test_requirements = [str(tr.req) for tr in parsed_test_requirements]

setup(
    name='my_checker',
    version='0.1.0',
    description='QQuuick math checker',
    long_description=readme + '\n\n' + doclink + '\n\n' + history,
    author='Michael Reuter',
    author_email='mareuternh@gmail.com',
    url='https://github.com/mareuter/my_checker',
    packages=[
        'my_checker',
    ],
    package_dir={'my_checker': 'my_checker'},
    include_package_data=True,
    install_requires=requirements,
    license='MIT',
    zip_safe=False,
    keywords='my_checker',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: Implementation :: PyPy',
    ],
    test_suite='tests',
    tests_require=test_requirements

)
