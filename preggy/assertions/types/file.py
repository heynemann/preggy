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

try:
    import six
except ImportError:  # pragma: no cover
    import warnings
    warnings.warn("Ignoring six. Probably setup.py installing package.")

try:
    import io
except ImportError:  # pragma: no cover
    ## FIXME: explain using "pass" here
    pass

from os.path import isfile
import types

from preggy import create_assertions


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
@create_assertions
def to_be_a_file(topic):
    '''Asserts that `topic` is a file.

    If `topic` is a string, this asserts that `os.path.isfile()`
    returns `True`.

    Otherwise, this asserts whether `topic` is an instance of the
    built-in `file` type.

    '''
    if _is_string(topic):
        return _is_file(topic)
    return _is_file_obj(topic)
