#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''preggy instance assertions.  For use with `expect()` (see `preggy.core`).
'''

# preggy assertions
# https://github.com/heynemann/preggy

# Licensed under the MIT license:
# http://www.opensource.org/licenses/mit-license
# Copyright (c) 2013 Bernardo Heynemann heynemann@gmail.com

import inspect

from preggy import assertion


@assertion
def to_be_instance_of(topic, expected):
    '''Asserts that `topic` is an instance of `expected`.'''
    if topic == expected:
        return True

    if (inspect.isclass(topic) and inspect.isclass(expected)) and issubclass(topic, expected):
        return True

    if isinstance(topic, expected):
        return True

    raise AssertionError(
        'Expected topic({0}) to be an instance of {1}, but it was a {2}',
        topic,
        expected,
        topic.__class__
    )


@assertion
def not_to_be_instance_of(topic, expected):
    '''Asserts that `topic` is NOT an instance of `expected`.'''
    try:
        to_be_instance_of(topic, expected)
    except AssertionError:
        return True

    raise AssertionError('Expected topic({0}) not to be an instance of {1}', topic, expected)
