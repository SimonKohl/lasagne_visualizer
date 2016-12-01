#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup
from pip.req import parse_requirements
from pip.download import PipSession



with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

# with open(fn) as f:
#     requirements = f.read().splitlines()
#
# test_requirements = []
# # # parse_requirements() returns generator of pip.req.InstallRequirement objects
# # install_reqs = parse_requirements('requirements_dev.txt', session=PipSession())
# #
# # # reqs is a list of requirement
# # # e.g. ['django==1.5.1', 'mezzanine==1.4.6']
# # test_requirements = [str(ir.req) for ir in install_reqs]
# #
# requirements = test_requirements

requirements = [
"alabaster==0.7.9", "argh==0.26.2", "arrow==0.10.0", "Babel==2.3.4", "binaryornot==0.4.0", "bumpversion==0.5.3", "cffi==1.9.1",\
"chardet==2.3.0", "click==6.6", "cookiecutter==1.4.0", "coverage==4.1", "cryptography==1.4", "cycler==0.10.0", "docutils==0.12",\
"enum34==1.1.6", "flake8==2.6.0", "future==0.16.0", "idna==2.1", "imagesize==0.7.1", "ipaddress==1.0.17", "Jinja2==2.8", "jinja2-time==0.2.0",\
"Lasagne==0.1", "MarkupSafe==0.23", "matplotlib==1.5.3", "mccabe==0.5.2", "numpy==1.11.2", "pandas==0.19.1", "pathtools==0.1.2", "pluggy==0.3.1",\
"poyo==0.4.0", "py==1.4.31", "pyasn1==0.1.9", "pycodestyle==2.0.0", "pycparser==2.17", "pyflakes==1.2.3", "Pygments==2.1.3", "pyparsing==2.1.10",\
"python-dateutil==2.6.0", "pytz==2016.7", "PyYAML==3.11", "seaborn==0.7.1", "six==1.10.0", "snowballstemmer==1.2.1", "Sphinx==1.4.8", "Theano==0.8.2",\
"tox==2.3.1", "virtualenv==15.1.0", "watchdog==0.8.3", "whichcraft==0.4.0"
]

test_requirements = requirements

setup(
    name='lasagne_visualizer',
    version='0.1.0',
    description="A tiny package to enable live-visualization of weight learning using lasagne models in ipython notebook.",
    long_description=readme + '\n\n' + history,
    author="Simon Kohl",
    author_email='simon.kohl@dkfz.de',
    url='https://github.com/SimonKohl/lasagne_visualizer',
    packages=[
        'lasagne_visualizer',
    ],
    package_dir={'lasagne_visualizer':
                 'lasagne_visualizer'},
    include_package_data=True,
    install_requires=requirements,
    license="MIT license",
    zip_safe=False,
    keywords='lasagne_visualizer',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3'
    ],
    test_suite='tests',
    tests_require=test_requirements
)
