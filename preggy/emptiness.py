# -*- coding: utf-8 -*-
'''preggy emptiness assertion.  For use with `expect()` (see `preggy.core`).'''


# preggy assertions
# https://github.com/heynemann/preggy

# Licensed under the MIT license:
# http://www.opensource.org/licenses/mit-license
# Copyright (c) 2013 Bernardo Heynemann heynemann@gmail.com

from preggy import create_assertions


@create_assertions
def to_be_empty(topic):
    '''Asserts that the `len` of `topic` is `0`.'''
    return len(topic) == 0
