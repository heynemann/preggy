# -*- coding: utf-8 -*-
'''preggy error assertions.  For use with `expect()` (see `preggy.core`).
'''

# preggy assertions
# https://github.com/heynemann/preggy

# Licensed under the MIT license:
# http://www.opensource.org/licenses/mit-license
# Copyright (c) 2013 Bernardo Heynemann heynemann@gmail.com

import inspect

from preggy import assertion, create_assertions


@assertion
def to_be_an_error_like(topic, expected):
    '''Asserts that `topic` is an instance (or subclass) of type `expected`.'''
    if not isinstance(topic, expected):
        raise AssertionError(
            'Expected topic({0}) to be an error of type {1}, but it was a {2}',
            topic, expected, topic.__class__
        )


@assertion
def to_have_an_error_message_of(topic, expected):
    '''Asserts that `topic` has an error message of `expected`.'''
    if str(topic) != expected:
        raise AssertionError('Expected topic({0}) to be an error with message {1}', topic, expected)


@create_assertions
def to_be_an_error(topic):
    '''Asserts that `topic` is an error.'''
    return topic and (isinstance(topic, Exception) or (inspect.isclass(topic) and issubclass(topic, Exception)))
