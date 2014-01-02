# -*- coding: utf-8 -*-
'''preggy instance assertions.  For use with `expect()` (see `preggy.core`).
'''

# preggy assertions
# https://github.com/heynemann/preggy

# Licensed under the MIT license:
# http://www.opensource.org/licenses/mit-license
# Copyright (c) 2013 Bernardo Heynemann heynemann@gmail.com

from __future__ import absolute_import
import inspect

from preggy import assertion


@assertion
def to_be_instance_of(topic, expected):
    '''Asserts that `topic` is an instance of `expected`.'''
    TRUE_CONDITIONS = (
        topic == expected,
        isinstance(topic, expected),
        (inspect.isclass(topic) and inspect.isclass(expected)) and issubclass(topic, expected),
    )
    if any(TRUE_CONDITIONS):
        return True
    msg = 'Expected topic({0}) to be an instance of {1}, but it was a {2}'.format(
        topic,
        expected,
        topic.__class__)
    raise AssertionError(msg)


@assertion
def not_to_be_instance_of(topic, expected):
    '''Asserts that `topic` is NOT an instance of `expected`.'''
    try:
        to_be_instance_of(topic, expected)
    except AssertionError:
        return True
    msg = 'Expected topic({0}) not to be an instance of {1}'.format(topic, expected)
    raise AssertionError(msg)
