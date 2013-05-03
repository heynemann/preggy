# -*- coding: utf-8 -*-
'''preggy equality assertion.  For use with `expect()` (see `preggy.core`).
'''


# preggy assertions
# https://github.com/heynemann/preggy

# Licensed under the MIT license:
# http://www.opensource.org/licenses/mit-license
# Copyright (c) 2013 Bernardo Heynemann heynemann@gmail.com

try:
    import six
except ImportError:
    print("Ignoring six. Probably setup.py installing package.")

from preggy import create_assertions


@create_assertions
def to_equal(topic, expected):
    '''Asserts that `topic == expected`.'''

    if isinstance(topic, six.string_types + (six.binary_type, )):
        topic = six.b(topic)

    if isinstance(expected, six.string_types + (six.binary_type, )):
        expected = six.b(expected)

    return expected == topic
