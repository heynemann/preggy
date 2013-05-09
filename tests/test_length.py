# -*- coding: utf-8 -*-

# preggy assertions
# https://github.com/heynemann/preggy

# Licensed under the MIT license:
# http://www.opensource.org/licenses/mit-license
# Copyright (c) 2013 Bernardo Heynemann heynemann@gmail.com

import sys
try:
    from Queue import LifoQueue
except ImportError:
    from queue import LifoQueue

from preggy import expect

queue = LifoQueue()
queue.put(1)
queue.put(2)
queue.put(3)

TEST_DATA = (
    "12345",
    [1, 2, 3],
    {"a": 1, "b": 2},
    tuple([1, 2, 3, 4, 5, 6]),
    queue
)

EXPECTED_DATA = (
    5,
    3,
    2,
    6,
    3
)

NOT_EXPECTED_DATA = (
    7,
    2,
    3,
    5,
    5
)


def is_expected(item, expected):
    expect(item).to_length(expected)
    try:
        expect(item).not_to_length(expected)
    except AssertionError:
        return
    assert False, "Should not have gotten this far"


def is_not_expected(item, expected):
    expect(item).Not.to_length(expected)
    expect(item).not_to_length(expected)

    try:
        expect(item).to_length(expected)
    except AssertionError:
        return
    assert False, "Should not have gotten this far"


def test_length():
    for index, item in enumerate(TEST_DATA):
        yield is_expected, item, EXPECTED_DATA[index]


def test_not_includes():
    for index, item in enumerate(TEST_DATA):
        yield is_not_expected, item, NOT_EXPECTED_DATA[index]


def test_unable_to_identify_length():
    try:
        expect(object()).to_length(1)
    except AssertionError:
        exc = sys.exc_info()[1]
        expect(str(exc)).to_match("Could not determine \"<object object at .+\"'s length.")
        return

    assert False, "Should not have gotten this far"


def test_unable_to_identify_not_length():
    try:
        expect(object()).not_to_length(1)
    except AssertionError:
        exc = sys.exc_info()[1]
        expect(str(exc)).to_match("Could not determine \"<object object at .+\"'s length.")
        return

    assert False, "Should not have gotten this far"
