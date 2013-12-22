# -*- coding: utf-8 -*-
'''preggy comparison assertion.  For use with `expect()` (see `preggy.core`).
'''


# preggy assertions
# https://github.com/heynemann/preggy

# Licensed under the MIT license:
# http://www.opensource.org/licenses/mit-license
# Copyright (c) 2013 Bernardo Heynemann heynemann@gmail.com

from __future__ import absolute_import

from preggy import create_assertions, fix_string


@create_assertions
def to_be_greater_than(topic, expected):
    '''Asserts that `topic > expected`.'''
    topic = fix_string(topic)
    expected = fix_string(expected)

    if isinstance(expected, (tuple, list, set, dict)):
        return len(topic) > len(expected)

    return topic > expected


@create_assertions
def to_be_lesser_than(topic, expected):
    '''Asserts that `topic < expected`.'''
    topic = fix_string(topic)
    expected = fix_string(expected)

    if isinstance(expected, (tuple, list, set, dict)):
        return len(topic) < len(expected)

    return topic < expected


@create_assertions
def to_be_greater_or_equal_to(topic, expected):
    '''Asserts that `topic >= expected`.'''
    topic = fix_string(topic)
    expected = fix_string(expected)

    if isinstance(expected, (tuple, list, set, dict)):
        return len(topic) >= len(expected)

    return topic >= expected


@create_assertions
def to_be_lesser_or_equal_to(topic, expected):
    '''Asserts that `topic <= expected`.'''
    topic = fix_string(topic)
    expected = fix_string(expected)

    if isinstance(expected, (tuple, list, set, dict)):
        return len(topic) <= len(expected)

    return topic <= expected
