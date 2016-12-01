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
    # TODO: put package requirements here
]
test_requirements = [
    # TODO: put package test requirements here
]

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
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    test_suite='tests',
    tests_require=test_requirements
)
