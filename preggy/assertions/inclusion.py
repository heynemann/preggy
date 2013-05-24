# -*- coding: utf-8 -*-
'''preggy inclusion assertion.  For use with `expect()` (see `preggy.core`).
'''


# preggy assertions
# https://github.com/heynemann/preggy

# Licensed under the MIT license:
# http://www.opensource.org/licenses/mit-license
# Copyright (c) 2013 Bernardo Heynemann heynemann@gmail.com

from preggy import create_assertions


@create_assertions
def to_include(topic, expected):
    '''Asserts that `expected` is in `topic`.'''
    if isinstance(topic, str):
        return str(expected) in topic
    return expected in topic
