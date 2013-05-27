# -*- coding: utf-8 -*-
'''preggy error assertions.  For use with `expect()` (see `preggy.core`).
'''

# preggy assertions
# https://github.com/heynemann/preggy

# Licensed under the MIT license:
# http://www.opensource.org/licenses/mit-license
# Copyright (c) 2013 Bernardo Heynemann heynemann@gmail.com

from __future__ import absolute_import
import inspect

from preggy import assertion, create_assertions


@assertion
def to_be_an_error_like(topic, expected):
    '''Asserts that `topic` is an instance (or subclass) of type `expected`.'''
    if not isinstance(topic, expected):
        msg = 'Expected topic({0}) to be an error of type {1}, but it was a {2}'
        values = topic, expected, topic.__class__
        err = AssertionError(msg.format(*values), *values)
        raise err


@assertion
def to_have_an_error_message_of(topic, expected):
    '''Asserts that `topic` has an error message of `expected`.'''
    if str(topic) != expected:
        msg = 'Expected topic({0!r}) to be an error with message {1!r}'
        values = str(topic), expected
        err = AssertionError(msg.format(*values))
        raise err


@create_assertions
def to_be_an_error(topic):
    '''Asserts that `topic` is an error.'''
    return isinstance(topic, BaseException)
