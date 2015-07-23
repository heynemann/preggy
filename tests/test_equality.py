# -*- coding: utf-8 -*-

# preggy assertions
# https://github.com/heynemann/preggy

# Licensed under the MIT license:
# http://www.opensource.org/licenses/mit-license
# Copyright (c) 2013 Bernardo Heynemann heynemann@gmail.com

from preggy import expect

from tests import Comparable, AnotherComparable

#-----------------------------------------------------------------------------

TEST_DATA = (
    'qwe',
    b'qwe',
    b'\xff\xd8\xff\xe0\x00\x10JFIF',
    [1],
    {'a': 'b'},
    tuple([2]),
    Comparable()
)

UNICODE_TEST_DATA = (
    b'asdqwe123',
    'asdqwe123',
)

UNEQUAL_DATA = (
    'asd',
    [2],
    {'c': 'd'},
    tuple([3]),
    Comparable('baz'),
    AnotherComparable()
)

#-----------------------------------------------------------------------------


def is_equal(topic):
    item, expected = topic
    expect(item).to_equal(expected)


def is_not_equal(topic):
    item, expected = topic
    expect(item).Not.to_equal(expected)
    expect(item).not_to_equal(expected)


#-----------------------------------------------------------------------------


def test_unicode_equal():
    is_equal((UNICODE_TEST_DATA[0], UNICODE_TEST_DATA[1]))


def test_equal():
    for item in TEST_DATA:
        yield is_equal, (item, item)


def test_not_equal():
    for item in TEST_DATA:
        for unequal in UNEQUAL_DATA:
            yield is_not_equal, (item, unequal)
