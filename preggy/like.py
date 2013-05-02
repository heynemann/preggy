#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''preggy like assertions.  For use with `expect()` (see `preggy.core`).
'''


# preggy assertions
# https://github.com/heynemann/preggy

# Licensed under the MIT license:
# http://www.opensource.org/licenses/mit-license
# Copyright (c) 2013 Bernardo Heynemann heynemann@gmail.com

try:
    from six import string_types, binary_type
except ImportError:
    print ("Ignoring six. Probably setup.py installing package.")

import numbers

from preggy import create_assertions


@create_assertions
def to_be_like(topic, expected):
    '''Asserts that `topic` is like (similar to) `expected`. Allows
    some leeway.

    '''
    return match_alike(expected, topic)


def match_alike(expected, topic):
    '''Asserts the "like"-ness of `topic` and `expected` according
    to their types.

    '''
    if topic is None:
        return expected is None

    if isinstance(topic, string_types + (binary_type, )):
        return compare_strings(expected, topic)

    if isinstance(topic, numbers.Number):
        return compare_numbers(expected, topic)

    if isinstance(topic, (list, tuple)):
        return compare_lists(expected, topic)

    if isinstance(topic, dict):
        return compare_dicts(expected, topic)

    raise RuntimeError('Could not compare {expected} and {topic}'.format(expected=expected, topic=topic))


def compare_strings(expected, topic):
    '''Asserts the "like"-ness of `topic` and `expected` as strings.
    Allows some leeway.  (Strings don't have to exactly match.)

    '''
    replaced_topic = topic.lower().replace(' ', '').replace('\n', '')
    replaced_expected = expected.lower().replace(' ', '').replace('\n', '')
    return replaced_expected == replaced_topic


def compare_numbers(expected, topic):
    '''Asserts the "like"-ness of `topic` and `expected` as Numbers.'''
    if not isinstance(topic, numbers.Number) or not isinstance(expected, numbers.Number):
        return False
    return float(expected) == float(topic)


def compare_dicts(expected, topic):
    '''Asserts the "like"-ness of `topic` and `expected` as dicts.'''
    return match_dicts(expected, topic) and match_dicts(topic, expected)


def match_dicts(expected, topic):
    '''Asserts the "like"-ness of all keys and values in `topic` and
    `expected`.
    '''
    for k, v in expected.items():
        if not k in topic or not match_alike(topic[k], v):
            return False
    return True


def compare_lists(expected, topic):
    '''Asserts the "like"-ness of `topic` and `expected` as lists.'''
    return match_lists(expected, topic) and match_lists(topic, expected)


def match_lists(expected, topic):
    '''Asserts the "like"-ness each item in of `topic` and `expected`
    (as lists or tuples).

    '''
    for item in expected:
        if isinstance(item, (list, tuple)):
            found = False
            for inner_item in topic:
                if isinstance(inner_item, (list, tuple)) and compare_lists(item, inner_item):
                    found = True
                    break
            if not found:
                return False
        elif not item in topic:
            return False

    return True
