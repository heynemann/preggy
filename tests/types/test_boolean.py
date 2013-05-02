# -*- coding: utf-8 -*-

# preggy assertions
# https://github.com/heynemann/preggy

# Licensed under the MIT license:
# http://www.opensource.org/licenses/mit-license
# Copyright (c) 2013 Bernardo Heynemann heynemann@gmail.com

from preggy import expect


EXPECTED_TEST_DATA = [
    True,
    "qwe",
    1,
    [1],
    tuple([1]),
    {"a": "b"}
]

NOT_EXPECTED_TEST_DATA = [
    False,
    "",
    0,
    [],
    tuple([]),
    {}
]


def is_true(item):
    expect(item).to_be_true()
    try:
        expect(item).not_to_be_true()
    except AssertionError:
        return
    assert False, "Should not have gotten this far"


def is_not_true(item):
    expect(item).Not.to_be_true()
    expect(item).not_to_be_true()

    try:
        expect(item).to_be_true()
    except AssertionError:
        return
    assert False, "Should not have gotten this far"


def is_false(item):
    expect(item).to_be_false()
    try:
        expect(item).not_to_be_false()
    except AssertionError:
        return
    assert False, "Should not have gotten this far"


def is_not_false(item):
    expect(item).Not.to_be_false()
    expect(item).not_to_be_false()

    try:
        expect(item).to_be_false()
    except AssertionError:
        return
    assert False, "Should not have gotten this far"


def test_to_be_true():
    for item in EXPECTED_TEST_DATA:
        yield is_true, item


def test_not_to_be_true():
    for item in NOT_EXPECTED_TEST_DATA:
        yield is_not_true, item


def test_to_be_false():
    for item in NOT_EXPECTED_TEST_DATA:
        yield is_false, item


def test_not_to_be_false():
    for item in EXPECTED_TEST_DATA:
        yield is_not_false, item
