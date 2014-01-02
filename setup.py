#!/usr/bin/env python
# -*- coding: utf-8 -*-

# preggy assertions
# https://github.com/heynemann/preggy

# Licensed under the MIT license:
# http://www.opensource.org/licenses/mit-license
# Copyright (c) 2011 Bernardo Heynemann heynemann@gmail.com

from setuptools import setup, find_packages
from preggy import __version__

test_requires = [
    'nose',
    'yanc',
    'coverage',
    'tox',
]

setup(
    name='preggy',
    version=__version__,
    description='preggy is an assertion library extracted from PyVows',
    long_description='''
        preggy is an assertion library extracted from PyVows.

        For more info, check out Preggy’s homepage: http://heynemann.github.io/preggy

        ''',
    keywords='test testing assert assertion development',
    
    author='Bernardo Heynemann',
    author_email='heynemann@gmail.com',
    maintainer='Zearin',
    maintainer_email='zearin@gonk.net',
    
    url='http://heynemann.github.io/preggy',
    download_url='https://github.com/heynemann/preggy/releases/tag/{version}'.format(version=__version__),

    ### For future, when Python packaging gets its crap together. See:
    ###   http://stackoverflow.com/questions/14459828/how-to-set-bug-tracker-url-in-setup-py-script
    #bugtrack_url='http://github.com/heynemann/preggy/issues',

    license='MIT',
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
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Testing'
    ],

    packages=find_packages(),

    install_requires=['six', 'unidecode'],
    extras_require={
        'tests': test_requires,
    },

    entry_points={},
)
