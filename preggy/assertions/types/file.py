# -*- coding: utf-8 -*-
'''preggy file assertions.  For use with `expect()` (see `preggy.core`).

For these assertions, "file" can be either a string or a file object.  Since
a string is required to create a file object in the first place, these
assertions provide a convenient, flexible way to test whether a topic is
a "file" in your tests.

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

try:
    import io
except ImportError:  # pragma: no cover
    pass  ## FIXME: explain using "pass" here

from os.path import isfile
import types

from preggy import assertion


#-------------------------------------------------------------------------------------------------
# Helpers
#-------------------------------------------------------------------------------------------------
_is_file = lambda topic: isfile(topic)
_is_string = lambda topic: isinstance(topic, (six.string_types, six.text_type))

def _is_file_obj(topic):
    try:
        return isinstance(topic, types.FileType)
    except AttributeError:  # pragma: no cover
        # FIXME: add comment...
        #        what is this for?
        return isinstance(topic, io.IOBase)


#-------------------------------------------------------------------------------------------------
# Assertions
#-------------------------------------------------------------------------------------------------
@assertion
def to_be_a_file(topic):
    '''Asserts that `topic` is a file.

    If `topic` is a string, this asserts that `os.path.isfile()`
    returns `True`.

    Otherwise, this asserts whether `topic` is an instance of the
    built-in `file` type.

    '''
    if _is_string(topic) and _is_file(topic):
        return True
    elif _is_file_obj(topic):
        return True
    msg = 'Expected topic({0}) to be a file, but it was {1!r}'.format(topic, type(topic))
    raise AssertionError(msg)

@assertion
def not_to_be_a_file(topic):
    '''Asserts that `topic` is NOT a file.

    If `topic` is a string, this asserts that `os.path.isfile()`
    returns `False`.

    Otherwise, this asserts whether `topic` is NOT an instance of the
    built-in `file` type.

    '''
    try:
        to_be_a_file(topic)
    except AssertionError:
        return True
    msg = 'Expected topic({0}) not to be a file, but it was'.format(topic)
    raise AssertionError(msg)
    