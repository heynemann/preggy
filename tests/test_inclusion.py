# -*- coding: utf-8 -*-

# preggy assertions
# https://github.com/heynemann/preggy

# Licensed under the MIT license:
# http://www.opensource.org/licenses/mit-license
# Copyright (c) 2013 Bernardo Heynemann heynemann@gmail.com

from preggy import expect

from tests import Comparable, DictLike

#-----------------------------------------------------------------------------

TEST_DATA = (
    'my_string',
    [1, 2, 3, ],
    {'a': 1, 'b': 2},
    tuple([1, 2, 3]),
    '123',
    '3.14',
    (None, Comparable(), 'deliberately the last one'),
    DictLike({'foo': 'bar'})
)

INCLUDED_DATA = (
    'str',
    1,
    'a',
    2,
    1,
    3.1,
    'deliberately the last one',
    'foo'
)

NOT_INCLUDED_DATA = (
    'potatoh',
    4,
    'c',
    5,
    4,
    4.2,
    2.718281828,
    'bar'
)

#-----------------------------------------------------------------------------


def is_included(item, expected):
    expect(item).to_include(expected)


def is_not_included(item, expected):
    expect(item).Not.to_include(expected)
    expect(item).not_to_include(expected)

#-----------------------------------------------------------------------------


def test_includes():
    for index, item in enumerate(TEST_DATA):
        yield is_included, item, INCLUDED_DATA[index]


def test_not_includes():
    for index, item in enumerate(TEST_DATA):
        yield is_not_included, item, NOT_INCLUDED_DATA[index]
