#!/usr/bin/env python
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
    try:
        length = len(topic)
    except AttributeError:
        if hasattr(topic, 'qsize'):
            length = topic.qsize()
    except TypeError:
        if hasattr(topic, 'qsize'):
            length = topic.qsize()

    if length != expected:
        raise AssertionError('Expected topic({0}) to have {1} of length, but it has {2}', topic, expected, length)


@assertion
def not_to_length(topic, expected):
    '''Asserts that `len(topic)` != `expected`.'''
    try:
        length = len(topic)
    except AttributeError:
        if hasattr(topic, 'qsize'):
            length = topic.qsize()
    except TypeError:
        if hasattr(topic, 'qsize'):
            length = topic.qsize()

    if length == expected:
        raise AssertionError('Expected topic({0}) not to have {1} of length', topic, expected)
