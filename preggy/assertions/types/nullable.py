# -*- coding: utf-8 -*-
'''preggy "null" (None) assertions.  For use with `expect()` (see `preggy.core`).
'''

# preggy assertions
# https://github.com/heynemann/preggy

# Licensed under the MIT license:
# http://www.opensource.org/licenses/mit-license
# Copyright (c) 2013 Bernardo Heynemann heynemann@gmail.com

from __future__ import absolute_import
from preggy import assertion


@assertion
def to_be_null(topic):
    '''Asserts that `topic` is `None`.'''
    if topic is not None:
        msg = 'Expected topic({0}) to be None'.format(topic)
        raise AssertionError(msg)


@assertion
def not_to_be_null(topic):
    '''Asserts that `topic` is NOT `None`.'''
    if topic is None:
        msg = 'Expected topic({0}) not to be None'.format(topic)
        raise AssertionError(msg)
