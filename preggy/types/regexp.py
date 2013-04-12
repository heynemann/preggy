#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''preggy regular expression assertions.  For use with `expect()` (see `preggy.core`).
'''

# preggy assertions
# https://github.com/heynemann/preggy

# Licensed under the MIT license:
# http://www.opensource.org/licenses/mit-license
# Copyright (c) 2013 Bernardo Heynemann heynemann@gmail.com

import re

from preggy import assertion


@assertion
def to_match(topic, expected):
    '''Asserts that `topic` matches the regular expression
    `expected`.

    '''
    if not re.match(expected, topic):
        raise AssertionError('Expected topic({0}) to match the regular expression {1}', topic, expected)


@assertion
def not_to_match(topic, expected):
    '''Asserts that `topic` DOES NOT match the regular expression
    `expected`.

    '''
    if re.match(expected, topic):
        raise AssertionError('Expected topic({0}) not to match the regular expression {1}', topic, expected)
