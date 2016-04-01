# -*- coding: utf-8 -*-
'''preggy inclusion assertion.  For use with `expect()` (see `preggy.core`).
'''


# preggy assertions
# https://github.com/heynemann/preggy

# Licensed under the MIT license:
# http://www.opensource.org/licenses/mit-license
# Copyright (c) 2013 Bernardo Heynemann heynemann@gmail.com

from __future__ import absolute_import

try:
    import six
except ImportError:  # pragma: no cover
    import warnings
    warnings.warn("Ignoring six. Probably setup.py installing package.")

from preggy import create_assertions


@create_assertions
def to_include(topic, expected):
    '''Asserts that `expected` is in `topic`.'''
    if isinstance(topic, six.string_types + tuple([six.binary_type, six.text_type])):
        return str(expected) in topic
    try:
        return expected in topic
    except:
        for t in topic:
            try:
                if expected == t:
                    return True
            except:
                pass
        return False
