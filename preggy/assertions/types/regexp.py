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
    '''Asserts that `topic` matches the regular expression `expected`.'''
    if not re.match(expected, topic):
        msg = 'Expected topic({0!r}) to match the regular expression {1!r}'.format(topic, expected)
        raise AssertionError(msg)


@assertion
def not_to_match(topic, expected):
    '''Asserts that `topic` DOES NOT match the regular expression `expected`.'''
    if re.match(expected, topic):
        msg = 'Expected topic({0!r}) not to match the regular expression {1!r}'.format(topic, expected)
        raise AssertionError(msg)
