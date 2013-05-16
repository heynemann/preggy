# -*- coding: utf-8 -*-
'''preggy 'like' assertions.  For use with `expect()` (see `preggy.core`).
'''


# preggy assertions
# https://github.com/heynemann/preggy

# Licensed under the MIT license:
# http://www.opensource.org/licenses/mit-license
# Copyright (c) 2013 Bernardo Heynemann heynemann@gmail.com

import re
from datetime import datetime
import difflib

try:
    from six import string_types, binary_type
except ImportError:  # pragma: no cover
    import warnings
    warnings.warn("Ignoring six. Probably setup.py installing package.")

import numbers

from preggy import assertion

DATE_THRESHOLD = 5.0
RESET = "\033[m"
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"


#-------------------------------------------------------------------------------------------------
# Helpers
#-------------------------------------------------------------------------------------------------
REMOVE_COLORS_REGEX = re.compile(
    r'(\033|\x1b|\x03)'  # prefixes
    r'\['                # non-regex bracket
    r'[0-9]*m',          # suffix
    re.UNICODE
)
_filter_str = lambda s: s.strip().lower().replace(' ', '').replace('\n', '')


def compare(first, second):
    matcher = difflib.SequenceMatcher(None, first, second)
    first = get_match_for_text(matcher, first, True)
    second = get_match_for_text(matcher, second, True)

    return matcher, first, second


def get_match_for_text(matcher, text, first):
    result = []
    for tag, i1, i2, j1, j2 in matcher.get_opcodes():

        if tag == 'delete':
            if first:
                result.append("%s%s%s" % (RED, text[i1:i2], RESET))
            else:
                result.append("%s%s%s" % (RED, text[j1:j2], RESET))

        elif tag == 'equal':
            if first:
                result.append(text[i1:i2])
            else:
                result.append(text[j1:j2])

        elif tag == 'insert':
            if first:
                result.append("%s%s%s" % (GREEN, text[i1:i2], RESET))
            else:
                result.append("%s%s%s" % (GREEN, text[j1:j2], RESET))

        elif tag == 'replace':
            if first:
                result.append("%s%s%s" % (YELLOW, text[i1:i2], RESET))
            else:
                result.append("%s%s%s" % (YELLOW, text[j1:j2], RESET))

    return "".join(result)


def _match_alike(expected, topic):
    '''Asserts the "like"-ness of `topic` and `expected` according to their types.'''
    if topic is None:
        return expected is None
    if isinstance(topic, string_types + (binary_type, )):
        return _compare_strings(expected, topic)
    if isinstance(topic, numbers.Number):
        return _compare_numbers(expected, topic)
    if isinstance(topic, (list, tuple)):
        return _compare_lists(expected, topic)
    if isinstance(topic, dict):
        return _compare_dicts(expected, topic)
    if isinstance(topic, datetime):
        return _compare_datetime(expected, topic)
    raise RuntimeError('Could not compare {expected} and {topic}'.format(expected=expected, topic=topic))


def _strip_string(text):
    if isinstance(text, (binary_type, )):
        text = text.decode('utf-8')

    text = REMOVE_COLORS_REGEX.sub('', text)
    text = _filter_str(text)

    if isinstance(text, (binary_type, )):
        text = text.decode('utf-8')

    return text


def _compare_strings(expected, topic):
    '''Asserts the "like"-ness of `topic` and `expected` as strings.
    Allows some leeway.  (Strings don't have to exactly match.)

    '''
    topic = _strip_string(topic)
    expected = _strip_string(expected)

    return expected == _filter_str(topic)


def __timedelta_to_seconds(timedelta):
    ms   = 10 ** 6          # microseconds/second
    days = 24 * 60 * 60     # seconds/day
    
    ms_as_seconds   = float(timedelta.microseconds) / ms
    seconds         = float(timedelta.seconds)
    days_as_seconds = float(timedelta.days) * days
    total_seconds   = sum( (ms_as_seconds, 
                            seconds, 
                            days_as_seconds) )
    return abs(total_seconds)  # abs() comes last


def _compare_datetime(expected, topic):
    return __timedelta_to_seconds(topic - expected) <= DATE_THRESHOLD


def _compare_numbers(expected, topic):
    '''Asserts the "like"-ness of `topic` and `expected` as Numbers.'''
    FALSE_CONDITIONS = (not isinstance(topic, numbers.Number),
                        not isinstance(expected, numbers.Number), )
    if any(FALSE_CONDITIONS):
        return False
    return float(expected) == float(topic)


def _compare_dicts(expected, topic):
    '''Asserts the "like"-ness of `topic` and `expected` as dicts.'''
    return _match_dicts(expected, topic) and _match_dicts(topic, expected)


def _match_dicts(expected, topic):
    '''Asserts the "like"-ness of all keys and values in `topic` and `expected`.'''
    for k, v in expected.items():
        if not k in topic or not _match_alike(topic[k], v):
            return False
    return True


def _compare_lists(expected, topic):
    '''Asserts the "like"-ness of `topic` and `expected` as lists.'''
    return _match_lists(expected, topic) and _match_lists(topic, expected)


def _match_lists(expected, topic):
    '''Asserts the "like"-ness each item in of `topic` and `expected` (as lists or tuples).'''
    for item in expected:
        if isinstance(item, (list, tuple)):
            found = False
            for inner_item in topic:
                if isinstance(inner_item, (list, tuple)) and _compare_lists(item, inner_item):
                    found = True
                    break
            if not found:
                return False
        elif not item in topic:
            return False
    return True


#-------------------------------------------------------------------------------------------------
# Assertions
#-------------------------------------------------------------------------------------------------
@assertion
def to_be_like(topic, expected):
    '''Asserts that `topic` is like (similar to) `expected`. Allows some leeway.'''
    result = _match_alike(expected, topic)

    if not result:
        if isinstance(topic, string_types + (binary_type, )) and isinstance(expected, string_types + (binary_type, )):
            matcher, first, second = compare(_strip_string(topic), _strip_string(expected))
            print
            print "Expected strings to be equal, but they were different:"
            print first
            print second
            print
        raise AssertionError("Expected '%s' to be like '%s'." % (topic, expected))


@assertion
def not_to_be_like(topic, expected):
    '''Asserts that `topic` is like (similar to) `expected`. Allows some leeway.'''
    result = _match_alike(expected, topic)

    if result:
        raise AssertionError("Expected '%s' not to be like '%s'." % (topic, expected))
