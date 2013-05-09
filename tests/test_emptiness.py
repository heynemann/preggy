# -*- coding: utf-8 -*-

# preggy assertions
# https://github.com/heynemann/preggy

# Licensed under the MIT license:
# http://www.opensource.org/licenses/mit-license
# Copyright (c) 2013 Bernardo Heynemann heynemann@gmail.com

from preggy import expect

#-----------------------------------------------------------------------------

EMPTY_DATA = (
    "",
    [],
    {},
    tuple([])
)

NOT_EMPTY_DATA = (
    "qwe",
    [1],
    {"a": "b"},
    tuple([2])
)

#-----------------------------------------------------------------------------

def is_empty(item):
    expect(item).to_be_empty()


def is_not_empty(item):
    expect(item).Not.to_be_empty()
    expect(item).not_to_be_empty()

#-----------------------------------------------------------------------------

def test_emptiness_assertion_works():
    for empty_item in EMPTY_DATA:
        yield is_empty, empty_item


def test_not_emptiness_assertion_works():
    for not_empty_item in NOT_EMPTY_DATA:
        yield is_not_empty, not_empty_item
