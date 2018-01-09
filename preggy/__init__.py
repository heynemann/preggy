# -*- coding: utf-8 -*-
'''preggy is an assertion library for Python. (What were you ``expect()``ing?)


EXAMPLE
=======

    from preggy import expect

    def test_roses_are_red():
        rose = Rose()
        expect(rose.color).to_equal('red')

    def test_violets_are_not_red():
        violet = Violet()
        expect(violet.color).not_to_equal('red')


For more info:
http://heynemann.github.io/preggy

'''

# preggy assertions
# https://github.com/heynemann/preggy

# Licensed under the MIT license:
# http://www.opensource.org/licenses/mit-license
# Copyright (c) 2013 Bernardo Heynemann heynemann@gmail.com

# flake8: noqa

from __future__ import absolute_import


from preggy.core import (assertion, create_assertions, Expect as expect)
from preggy.__meta__ import __version__
try:
    from preggy.assertions import *
except (ImportError, KeyError):
    print('''
        Failed to import preggy's modules. If not in setup.py this is an error.
        Please report an issue in our Github Issues Page.
    ''')

__version__ = __version__
