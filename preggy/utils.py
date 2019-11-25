# -*- coding: utf-8 -*-
'''Assorted helpers used elsewhere in preggy.

Currently contains only string formatting code, but this may (or may not) change.
'''
# preggy assertions
# https://github.com/heynemann/preggy

# Licensed under the MIT license:
# http://www.opensource.org/licenses/mit-license
# Copyright (c) 2013 Bernardo Heynemann heynemann@gmail.com

from __future__ import absolute_import
import logging
import re

try:
    import six
    text_type = six.text_type
except ImportError:  # pragma: no cover
    import warnings
    warnings.warn('Ignoring six. Probably setup.py installing package.')

try:
    from unidecode import unidecode
except ImportError:  # pragma: no cover
    import warnings
    warnings.warn('Ignoring unidecode. Probably setup.py installing package.')


logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)

UNDERSCORES = re.compile(r'_+')

def humanized_name(thing):
    try:                    return UNDERSCORES.sub(' ', thing.__name__)
    except AttributeError:  return UNDERSCORES.sub(' ', thing)

def format_assertion_msg(assertion_clause, *args):
    raw_msg = 'Expected topic({{0!r}}) {assertion_clause}'
    raw_msg = raw_msg.format(assertion_clause=assertion_clause)
    if len(args) == 2:
        raw_msg += ' {1!r}'
    return raw_msg

def fix_string(obj):
    if isinstance(obj, (six.binary_type, )):
        try:
            return obj.decode('utf-8')
        except Exception:
            return obj
    return obj


class AssertionsMap(dict):
    '''A simple dict with a dash of logging.'''

    def __getitem__(self, k):
        # log.debug('fetching assertion: {name!r}'.format(name=k))
        return super(AssertionsMap, self).__getitem__(k)

    def __setitem__(self, k, v):
        _keys = self.keys()
        # commented due to noise in tests
        # if k not in _keys:
            # log.debug('registering assertion: {name!r}, with function: {func!r}'.format(name=k, func=v))
        # elif self[k] is not v:  # existing key with new assertion function
            # log.debug('re-registering assertion: {name!r}, with new function: {func!r}'.format(name=k, func=v))
        # elif self[k] is v:  # same key, same function
            # return
        if k in _keys and self[k] is v:  # same key, same function
            return
        return super(AssertionsMap, self).__setitem__(k, v)

    def __delitem__(self, k):
        # log.debug('deleting assertion: {name!r}'.format(name=k))
        return super(AssertionsMap, self).__delitem__(k)
