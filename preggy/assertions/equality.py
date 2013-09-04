# -*- coding: utf-8 -*-
'''preggy equality assertion.  For use with `expect()` (see `preggy.core`).
'''


# preggy assertions
# https://github.com/heynemann/preggy

# Licensed under the MIT license:
# http://www.opensource.org/licenses/mit-license
# Copyright (c) 2013 Bernardo Heynemann heynemann@gmail.com

from __future__ import absolute_import

from preggy import create_assertions, fix_string


@create_assertions
def to_equal(topic, expected):
    '''Asserts that `topic == expected`.'''
    topic = fix_string(topic)
    expected = fix_string(expected)

    return expected == topic
