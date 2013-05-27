# -*- coding: utf-8 -*-
'''preggy function assertions.  For use with `expect()` (see `preggy.core`).
'''

# preggy assertions
# https://github.com/heynemann/preggy

# Licensed under the MIT license:
# http://www.opensource.org/licenses/mit-license
# Copyright (c) 2013 Bernardo Heynemann heynemann@gmail.com


from __future__ import absolute_import
import inspect

from preggy import assertion

#-------------------------------------------------------------------------------------------------
# Helpers
#-------------------------------------------------------------------------------------------------
_is_func = lambda topic: inspect.ismethod(topic) or inspect.isfunction(topic)


#-------------------------------------------------------------------------------------------------
# Assertions
#-------------------------------------------------------------------------------------------------
@assertion
def to_be_a_function(topic):
    '''Asserts that `topic` is a function.'''
    if not _is_func(topic):
        msg = 'Expected topic({0}) to be a function or a method, but it was a {1}'.format(
            topic, 
            topic.__class__
            )
        raise AssertionError(msg)


@assertion
def not_to_be_a_function(topic):
    '''Asserts that `topic` is NOT a function.'''
    if _is_func(topic):
        msg = 'Expected topic({0}) not to be a function or a method'.format(topic)
        raise AssertionError(msg)
