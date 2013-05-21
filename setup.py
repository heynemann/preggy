#!/usr/bin/env python
# -*- coding: utf-8 -*-

# preggy assertions
# https://github.com/heynemann/preggy

# Licensed under the MIT license:
# http://www.opensource.org/licenses/mit-license
# Copyright (c) 2011 Bernardo Heynemann heynemann@gmail.com

from setuptools import setup
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
        
        For more info, check out Preggy’s homepage: http://heynemann.github.io/preggy/ 

        ''',
    keywords='test testing assert assertion development',
    author='Bernardo Heynemann',
    author_email='heynemann@gmail.com',
    contributor='Zearin',
    contributor_email='zearin@gonk.net',
    url='http://github.com/heynemann/preggy/',
    download_url='http://heynemann.github.io/preggy/',
    license='MIT',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: MacOS',
        'Operating System :: POSIX',
        'Operating System :: Unix',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Topic :: Software Development :: Testing'
    ],
    
    packages=['preggy', 'preggy.assertions', 'preggy.assertions.types'],
    
    install_requires=['six'],
    
    extras_require={
        'tests': test_requires,
    },
    
    entry_points={},
)
