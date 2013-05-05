# -*- coding: utf-8 -*-
'''preggy boolean assertions.  For use with `expect()` (see `preggy.core`).
'''

# preggy assertions
# https://github.com/heynemann/preggy

# Licensed under the MIT license:
# http://www.opensource.org/licenses/mit-license
# Copyright (c) 2013 Bernardo Heynemann heynemann@gmail.com

from preggy import assertion


@assertion
def to_be_true(topic):
    '''Asserts that the boolean value of `topic` is `True`.'''
    if not bool(topic):
        msg = 'Expected topic({0}) to be truthy'.format(topic)
        raise AssertionError(msg)


@assertion
def to_be_false(topic):
    '''Asserts that the boolean value of `topic` is `False`.'''
    if bool(topic):
        msg = 'Expected topic({0}) to be falsy'.format(topic)
        raise AssertionError(msg)


@assertion
def not_to_be_true(topic):
    return to_be_false(topic)


@assertion
def not_to_be_false(topic):
    return to_be_true(topic)
