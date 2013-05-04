# -*- coding: utf-8 -*-
'''preggy length assertions.  For use with `expect()` (see `preggy.core`).
'''


# preggy assertions
# https://github.com/heynemann/preggy

# Licensed under the MIT license:
# http://www.opensource.org/licenses/mit-license
# Copyright (c) 2013 Bernardo Heynemann heynemann@gmail.com

from preggy import assertion


@assertion
def to_length(topic, expected):
    '''Asserts that `len(topic)` == `expected`.'''
    length = None

    try:
        length = len(topic)
    except (AttributeError, TypeError):
        if hasattr(topic, 'qsize'):
            length = topic.qsize()

    if length is None:
        raise AssertionError("Could not determine \"{0}\"'s length.".format(topic))

    if length != expected:
        raise AssertionError('Expected "{0}" to have {1} of length, but it has {2}'.format(topic, expected, length))


@assertion
def not_to_length(topic, expected):
    '''Asserts that `len(topic)` != `expected`.'''

    length = None

    try:
        length = len(topic)
    except (AttributeError, TypeError):
        if hasattr(topic, 'qsize'):
            length = topic.qsize()

    if length is None:
        raise AssertionError("Could not determine \"{0}\"'s length.".format(topic))

    if length == expected:
        raise AssertionError('Expected {0} not to have {1} of length'.format(topic, expected))
