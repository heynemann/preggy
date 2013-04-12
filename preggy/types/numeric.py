#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''preggy numeric assertion.  For use with `expect()` (see `preggy.core`).
'''

# preggy assertions
# https://github.com/heynemann/preggy

# Licensed under the MIT license:
# http://www.opensource.org/licenses/mit-license
# Copyright (c) 2013 Bernardo Heynemann heynemann@gmail.com

import numbers

from preggy import create_assertions


@create_assertions
def to_be_numeric(topic):
    '''Asserts that `topic` is a Number.'''
    return isinstance(topic, numbers.Number)
