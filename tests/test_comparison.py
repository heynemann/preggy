# -*- coding: utf-8 -*-

# preggy assertions
# https://github.com/heynemann/preggy

# Licensed under the MIT license:
# http://www.opensource.org/licenses/mit-license
# Copyright (c) 2013 Bernardo Heynemann heynemann@gmail.com

from preggy import expect

#-----------------------------------------------------------------------------

TEST_DATA = (
    'qwe',
    5,
    {'a': 'b', 'c': 'd'},
    tuple([2, 3]),
    list([2, 3]),
    set([2, 3]),
)

GREATER_THAN_DATA = (
    'asd',
    2,
    {'c': 'd'},
    tuple([3]),
    list([3]),
    set([3]),
)

LESSER_THAN_DATA = (
    'zcs',
    7,
    {'a': 'b', 'c': 'd', 'e': 'f'},
    tuple([3, 4, 5]),
    list([3, 4, 5]),
    set([3, 4, 5]),
)

LESSER_OR_EQUAL_TO_DATA = (
    'qwe',
    5,
    {'a': 'b', 'c': 'd'},
    tuple([2, 3]),
    list([2, 3]),
    set([2, 3]),
)

NOT_LESSER_OR_EQUAL_TO_DATA = (
    'zcs',
    7,
    {'a': 'b', 'c': 'd', 'e': 'f'},
    tuple([3, 4, 5]),
    list([3, 4, 5]),
    set([3, 4, 5]),
)

LESSER_OR_EQUAL_TO_DATA_2 = (
    'zcs',
    7,
    {'a': 'b', 'c': 'd', 'e': 'f'},
    tuple([3, 4, 5]),
    list([3, 4, 5]),
    set([3, 4, 5]),
)

GREATER_OR_EQUAL_TO_DATA = (
    'qwe',
    5,
    {'a': 'b', 'c': 'd'},
    tuple([2, 3]),
    list([2, 3]),
    set([2, 3]),
)

NOT_GREATER_OR_EQUAL_TO_DATA = (
    'abc',
    1,
    {'a': 'b'},
    tuple([3]),
    list([3]),
    set([3]),
)

GREATER_OR_EQUAL_TO_DATA_2 = (
    'abc',
    1,
    {'a': 'b'},
    tuple([3]),
    list([3]),
    set([3]),
)


#-----------------------------------------------------------------------------


def is_greater_than(topic):
    item, expected = topic
    expect(item).to_be_greater_than(expected)


def is_not_greater_than(topic):
    item, expected = topic
    expect(item).Not.to_be_greater_than(expected)
    expect(item).not_to_be_greater_than(expected)


def is_lesser_than(topic):
    item, expected = topic
    expect(item).to_be_lesser_than(expected)


def is_not_lesser_than(topic):
    item, expected = topic
    expect(item).Not.to_be_lesser_than(expected)
    expect(item).not_to_be_lesser_than(expected)


def is_greater_or_equal_to(topic):
    item, expected = topic
    expect(item).to_be_greater_or_equal_to(expected)


def is_not_greater_or_equal_to(topic):
    item, expected = topic
    expect(item).Not.to_be_greater_or_equal_to(expected)
    expect(item).not_to_be_greater_or_equal_to(expected)


def is_lesser_or_equal_to(topic):
    item, expected = topic
    expect(item).to_be_lesser_or_equal_to(expected)


def is_not_lesser_or_equal_to(topic):
    item, expected = topic
    expect(item).Not.to_be_lesser_or_equal_to(expected)
    expect(item).not_to_be_lesser_or_equal_to(expected)


#-----------------------------------------------------------------------------


def test_greater_than():
    for index, item in enumerate(TEST_DATA):
        expected = GREATER_THAN_DATA[index]
        yield is_greater_than, (item, expected)


def test_not_greater_than():
    for index, item in enumerate(TEST_DATA):
        expected = GREATER_THAN_DATA[index]
        yield is_not_greater_than, (expected, item)


def test_lesser_than():
    for index, item in enumerate(TEST_DATA):
        expected = LESSER_THAN_DATA[index]
        yield is_lesser_than, (item, expected)


def test_not_lesser_than():
    for index, item in enumerate(TEST_DATA):
        expected = LESSER_THAN_DATA[index]
        yield is_not_lesser_than, (expected, item)


def test_greater_or_equal_to():
    for index, item in enumerate(TEST_DATA):
        expected = GREATER_OR_EQUAL_TO_DATA[index]
        yield is_greater_or_equal_to, (item, expected)

    for index, item in enumerate(TEST_DATA):
        expected = GREATER_OR_EQUAL_TO_DATA_2[index]
        yield is_greater_or_equal_to, (item, expected)


def test_not_greater_or_equal_to():
    for index, item in enumerate(TEST_DATA):
        expected = NOT_GREATER_OR_EQUAL_TO_DATA[index]
        yield is_not_greater_or_equal_to, (expected, item)

    for index, item in enumerate(TEST_DATA):
        expected = GREATER_OR_EQUAL_TO_DATA_2[index]
        yield is_not_greater_or_equal_to, (expected, item)


def test_lesser_or_equal_to():
    for index, item in enumerate(TEST_DATA):
        expected = LESSER_OR_EQUAL_TO_DATA[index]
        yield is_lesser_or_equal_to, (item, expected)

    for index, item in enumerate(TEST_DATA):
        expected = LESSER_OR_EQUAL_TO_DATA_2[index]
        yield is_lesser_or_equal_to, (item, expected)


def test_not_lesser_or_equal_to():
    for index, item in enumerate(TEST_DATA):
        expected = NOT_LESSER_OR_EQUAL_TO_DATA[index]
        yield is_not_lesser_or_equal_to, (expected, item)

    for index, item in enumerate(TEST_DATA):
        expected = LESSER_OR_EQUAL_TO_DATA_2[index]
        yield is_not_lesser_or_equal_to, (expected, item)
