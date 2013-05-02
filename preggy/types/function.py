# -*- coding: utf-8 -*-
'''preggy function assertions.  For use with `expect()` (see `preggy.core`).
'''

# preggy assertions
# https://github.com/heynemann/preggy

# Licensed under the MIT license:
# http://www.opensource.org/licenses/mit-license
# Copyright (c) 2013 Bernardo Heynemann heynemann@gmail.com

import inspect

from preggy import assertion


@assertion
def to_be_a_function(topic):
    '''Asserts that `topic` is a function.'''
    if not (inspect.ismethod(topic) or inspect.isfunction(topic)):
        raise AssertionError('Expected topic({0}) to be a function or a method, but it was a {1}', topic, topic.__class__)


@assertion
def not_to_be_a_function(topic):
    '''Asserts that `topic` is NOT a function.'''
    if inspect.ismethod(topic) or inspect.isfunction(topic):
        raise AssertionError('Expected topic({0}) not to be a function or a method', topic)
