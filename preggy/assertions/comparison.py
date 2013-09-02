# -*- coding: utf-8 -*-
'''preggy comparison assertion.  For use with `expect()` (see `preggy.core`).
'''


# preggy assertions
# https://github.com/heynemann/preggy

# Licensed under the MIT license:
# http://www.opensource.org/licenses/mit-license
# Copyright (c) 2013 Bernardo Heynemann heynemann@gmail.com

from __future__ import absolute_import

try:
    import six
except ImportError:  # pragma: no cover
    import warnings
    warnings.warn("Ignoring six. Probably setup.py installing package.")

from preggy import create_assertions


@create_assertions
def to_be_greater_than(topic, expected):
    '''Asserts that `topic > expected`.'''
    if isinstance(topic, (six.binary_type, )):
        topic = topic.decode('utf-8')
    if isinstance(expected, (six.binary_type, )):
        expected = expected.decode('utf-8')

    if isinstance(expected, (tuple, list, set, dict)):
        return len(topic) > len(expected)

    return topic > expected


@create_assertions
def to_be_lesser_than(topic, expected):
    '''Asserts that `topic < expected`.'''
    if isinstance(topic, (six.binary_type, )):
        topic = topic.decode('utf-8')
    if isinstance(expected, (six.binary_type, )):
        expected = expected.decode('utf-8')

    if isinstance(expected, (tuple, list, set, dict)):
        return len(topic) < len(expected)

    return topic < expected


@create_assertions
def to_be_greater_or_equal_to(topic, expected):
    '''Asserts that `topic < expected`.'''
    if isinstance(topic, (six.binary_type, )):
        topic = topic.decode('utf-8')
    if isinstance(expected, (six.binary_type, )):
        expected = expected.decode('utf-8')

    if isinstance(expected, (tuple, list, set, dict)):
        return len(topic) >= len(expected)

    return topic >= expected


@create_assertions
def to_be_lesser_or_equal_to(topic, expected):
    '''Asserts that `topic < expected`.'''
    if isinstance(topic, (six.binary_type, )):
        topic = topic.decode('utf-8')
    if isinstance(expected, (six.binary_type, )):
        expected = expected.decode('utf-8')

    if isinstance(expected, (tuple, list, set, dict)):
        return len(topic) <= len(expected)

    return topic <= expected
