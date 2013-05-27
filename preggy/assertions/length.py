# -*- coding: utf-8 -*-
'''preggy length assertions.  For use with `expect()` (see `preggy.core`).
'''


# preggy assertions
# https://github.com/heynemann/preggy

# Licensed under the MIT license:
# http://www.opensource.org/licenses/mit-license
# Copyright (c) 2013 Bernardo Heynemann heynemann@gmail.com

from __future__ import absolute_import
from preggy import assertion


#-------------------------------------------------------------------------------------------------
# Helpers
#-------------------------------------------------------------------------------------------------
def _get_length(topic, expected):
    length = None
    try:
        length = len(topic)
    except (AttributeError, TypeError):
        if hasattr(topic, 'qsize'):
            length = topic.qsize()
    if length is None:
        msg = "Could not determine \"{0}\"'s length.".format(topic)
        raise AssertionError(msg)
    return length


#-------------------------------------------------------------------------------------------------
# Assertions
#-------------------------------------------------------------------------------------------------
@assertion
def to_length(topic, expected):
    '''Asserts that `len(topic)` == `expected`.'''
    length = _get_length(topic, expected)
    if length != expected:
        msg = 'Expected topic({0!r}) to have {1} of length, but it has {2}'.format(topic, expected, length)
        raise AssertionError(msg)

@assertion
def not_to_length(topic, expected):
    '''Asserts that `len(topic)` != `expected`.'''
    length = _get_length(topic, expected)
    if length == expected:
        msg = 'Expected topic({0!r}) not to have {1} of length'.format(topic, expected)
        raise AssertionError(msg)
