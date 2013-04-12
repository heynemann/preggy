#!/usr/bin/env python
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

from os.path import isfile
import types

from preggy import assertion


# Helpers
_isfile = lambda topic: isfile(topic)
_is_file_obj = lambda topic: isinstance(topic, types.FileType)


@assertion
def to_be_a_file(topic):
    '''Asserts that `topic` is a file.

    If `topic` is a string, this asserts that `os.path.isfile()`
    returns `True`.

    Otherwise, this asserts whether `topic` is an instance of the
    built-in `file` type.

    '''
    VAE = AssertionError("Expected topic({0}) to be a file", topic)

    if isinstance(topic, basestring):
        if not _isfile(topic):
            raise VAE
    else:
        if not _is_file_obj(topic):
            raise VAE


@assertion
def not_to_be_a_file(topic):
    '''Asserts that `topic` is NOT a file.

     If `topic` is a string, this asserts whether `os.path.isfile()`
     returns `False`.

    Otherwise, this asserts whether `topic` is not an instance of the
    built-in `file` type.

    '''
    VAE = AssertionError("Expected topic({0}) not to be a file", topic)

    if isinstance(topic, basestring):
        if _isfile(topic):
            raise VAE
    else:
        if _is_file_obj(topic):
            raise VAE
