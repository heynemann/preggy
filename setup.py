#!/usr/bin/env python
# -*- coding: utf-8 -*-

# preggy assertions
# https://github.com/heynemann/preggy

# Licensed under the MIT license:
# http://www.opensource.org/licenses/mit-license
# Copyright (c) 2011 Bernardo Heynemann heynemann@gmail.com

from io import open
from os import path
from setuptools import setup, find_packages

from preggy import __meta__, __version__

REQUIREMENTS = {
    'install': ['six', 'unidecode'],
    'extras': {
        'tests':['nose', 'yanc', 'coverage', 'tox',]
    }
}

# read the contents of your README file
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name        ='preggy',
    version     =__version__,
    description ='preggy is an assertion library for Python.** What were you `expect`ing?',
    long_description=long_description,
    long_description_content_type='text/markdown',
    keywords    =__meta__.__keywords__,

    author      =__meta__.__author__,
    author_email=__meta__.__author_email__,

    maintainer  =__meta__.__maintainer__,
    maintainer_email=__meta__.__maintainer_email__,

    url         =__meta__.__url__,
    download_url=__meta__.__download_url__,

    ### For future, when Python packaging gets its crap together. See:
    ###   http://stackoverflow.com/questions/14459828/how-to-set-bug-tracker-url-in-setup-py-script
    #bugtrack_url='http://github.com/heynemann/preggy/issues',

    license     =__meta__.__license__,

    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: MacOS',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: POSIX',
        'Operating System :: Unix',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Testing'
    ],

    packages=find_packages(exclude=['tests', 'tests.*']),

    install_requires= REQUIREMENTS['install'],
    extras_require  = REQUIREMENTS['extras'],

    entry_points={},
)
