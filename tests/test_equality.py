# -*- coding: utf-8 -*-

# preggy assertions
# https://github.com/heynemann/preggy

# Licensed under the MIT license:
# http://www.opensource.org/licenses/mit-license
# Copyright (c) 2013 Bernardo Heynemann heynemann@gmail.com

from preggy import expect

#-----------------------------------------------------------------------------

TEST_DATA = (
    "qwe",
    [1],
    {"a": "b"},
    tuple([2])
)

UNEQUAL_DATA = (
    "asd",
    [2],
    {"c": "d"},
    tuple([3])
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

def test_equal():
    for item in TEST_DATA:
        yield is_equal, (item, item)


def test_not_equal():
    for item in TEST_DATA:
        for unequal in UNEQUAL_DATA:
            yield is_not_equal, (item, unequal)
