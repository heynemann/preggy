# -*- coding: utf-8 -*-

# preggy assertions
# https://github.com/heynemann/preggy

# Licensed under the MIT license:
# http://www.opensource.org/licenses/mit-license
# Copyright (c) 2013 Bernardo Heynemann heynemann@gmail.com

from preggy import expect

import pytest

#-----------------------------------------------------------------------------

TEST_DATA = (
    'qwe',
    b'qwe',
    5,
    {'a': 'b', 'c': 'd'},
    tuple([2, 3]),
    list([2, 3]),
    set([2, 3]),
)

GREATER_THAN_DATA = (
    'asd',
    b'asd',
    2,
    {'c': 'd'},
    tuple([3]),
    list([3]),
    set([3]),
)

LESSER_THAN_DATA = (
    'zcs',
    b'zcs',
    7,
    {'a': 'b', 'c': 'd', 'e': 'f'},
    tuple([3, 4, 5]),
    list([3, 4, 5]),
    set([3, 4, 5]),
)

LESSER_OR_EQUAL_TO_DATA = (
    'qwe',
    b'qwe',
    5,
    {'a': 'b', 'c': 'd'},
    tuple([2, 3]),
    list([2, 3]),
    set([2, 3]),
)

NOT_LESSER_OR_EQUAL_TO_DATA = (
    'zcs',
    b'zcs',
    7,
    {'a': 'b', 'c': 'd', 'e': 'f'},
    tuple([3, 4, 5]),
    list([3, 4, 5]),
    set([3, 4, 5]),
)

LESSER_OR_EQUAL_TO_DATA_2 = (
    'zcs',
    b'zcs',
    7,
    {'a': 'b', 'c': 'd', 'e': 'f'},
    tuple([3, 4, 5]),
    list([3, 4, 5]),
    set([3, 4, 5]),
)

GREATER_OR_EQUAL_TO_DATA = (
    'qwe',
    b'qwe',
    5,
    {'a': 'b', 'c': 'd'},
    tuple([2, 3]),
    list([2, 3]),
    set([2, 3]),
)

NOT_GREATER_OR_EQUAL_TO_DATA = (
    'abc',
    b'abc',
    1,
    {'a': 'b'},
    tuple([3]),
    list([3]),
    set([3]),
)

GREATER_OR_EQUAL_TO_DATA_2 = (
    'abc',
    b'abc',
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


@pytest.mark.parametrize("index,item", enumerate(TEST_DATA))
def test_greater_than(index, item):
    is_greater_than((item, GREATER_THAN_DATA[index]))


@pytest.mark.parametrize("index,item", enumerate(TEST_DATA))
def test_not_greater_than(index, item):
    is_not_greater_than((GREATER_THAN_DATA[index], item))


@pytest.mark.parametrize("index,item", enumerate(TEST_DATA))
def test_lesser_than(index, item):
    is_lesser_than((item, LESSER_THAN_DATA[index]))


@pytest.mark.parametrize("index,item", enumerate(TEST_DATA))
def test_not_lesser_than(index, item):
    is_not_lesser_than((LESSER_THAN_DATA[index], item))


@pytest.mark.parametrize("index,item", enumerate(TEST_DATA))
def test_greater_or_equal_to(index, item):
    expected = GREATER_OR_EQUAL_TO_DATA[index]
    is_greater_or_equal_to((item, expected))
    expected = GREATER_OR_EQUAL_TO_DATA_2[index]
    is_greater_or_equal_to((item, expected))


@pytest.mark.parametrize("index,item", enumerate(TEST_DATA))
def test_not_greater_or_equal_to(index, item):
    expected = NOT_GREATER_OR_EQUAL_TO_DATA[index]
    is_not_greater_or_equal_to((expected, item))
    expected = GREATER_OR_EQUAL_TO_DATA_2[index]
    is_not_greater_or_equal_to((expected, item))


@pytest.mark.parametrize("index,item", enumerate(TEST_DATA))
def test_lesser_or_equal_to(index, item):
    expected = LESSER_OR_EQUAL_TO_DATA[index]
    is_lesser_or_equal_to((item, expected))
    expected = LESSER_OR_EQUAL_TO_DATA_2[index]
    is_lesser_or_equal_to((item, expected))


@pytest.mark.parametrize("index,item", enumerate(TEST_DATA))
def test_not_lesser_or_equal_to(index, item):
    expected = NOT_LESSER_OR_EQUAL_TO_DATA[index]
    is_not_lesser_or_equal_to((expected, item))
    expected = LESSER_OR_EQUAL_TO_DATA_2[index]
    is_not_lesser_or_equal_to((expected, item))
