# -*- coding: utf-8 -*-

# preggy assertions
# https://github.com/heynemann/preggy

# Licensed under the MIT license:
# http://www.opensource.org/licenses/mit-license
# Copyright (c) 2013 Bernardo Heynemann heynemann@gmail.com

import sys
from datetime import datetime
from uuid import uuid4

from preggy import expect

#-----------------------------------------------------------------------------

STRING_TEST_DATA = b'asdqwe123'
EXPECTED_STRING_TEST_DATA = [
    'ASdQwE123',
    'ASDQWE123',
    'asdqwe123',
    '\tasd\nqwe\r123',
    '\033[0m\033[31masdqwe123\033[32m',
    '\x1b[0m\x1b[31masdqwe123\x1b[32m',
    '\x03[0m\x03[31masdqwe123\x03[32m',
    '\x1b[32;01masdqwe123\x1b[0m'
]
NOT_EXPECTED_STRING_TEST_DATA = [
    'ZASdQwE123',
    'ZASDQWE123',
    'Zasdqwe123',
]

NUMBER_TEST_DATA = 10.2345
EXPECTED_NUMBER_TEST_DATA = [
    10.23,
    10.23456,
    10.23457,
    10.23555
]
NOT_EXPECTED_NUMBER_TEST_DATA = [
    0,
    10.45,
    20
]

DATETIME_TEST_DATA = datetime(2010, 11, 12, 13, 14, 15, 123456)
EXPECTED_DATETIME_TEST_DATA = [
    datetime(2010, 11, 12, 13, 14, 15, 123456),
    datetime(2010, 11, 12, 13, 14, 16, 123456),
    datetime(2010, 11, 12, 13, 14, 15, 123457)
]
NOT_EXPECTED_DATETIME_TEST_DATA = [
    datetime(2010, 11, 12, 13, 15, 15, 123456),
    datetime(2010, 11, 12, 14, 14, 15, 123456),
    datetime(2010, 11, 13, 13, 14, 15, 123456),
    datetime(2010, 12, 12, 13, 14, 15, 123456),
    datetime(2011, 11, 12, 13, 14, 15, 123456),
]

LIST_TEST_DATA = [1, 2, 3, 4, 'a', 'b', [1, 2, 3], {'a': 1, 'b': 2}]
EXPECTED_LIST_TEST_DATA = [
    [1, 2, 3, 4, 'a', {'a': 1, 'b': 2}, 'b', [1, 2, 3]],
    [4, 3, {'b': 2, 'a': 1}, 2, 1, 'b', 'a', [3, 2, 1]],
    ['b', [3, 1, 2], 2, 1, {'a': 1, 'b': 2}, 4, 3, 'a']
]
NOT_EXPECTED_LIST_TEST_DATA = [
    [1, 2, 3, 4, 'a', 'b', [2, 3], {'a': 1, 'b': 2}],
    [9, 1, 2, 3, 4, 'a', {'a': 1, 'b': 2}, 'b', [1, 2, 3]],
    [9, 4, 3, {'b': 2, 'a': 1}, 2, 1, 'b', 'a', [3, 2, 1]],
    [9, 'b', [3, 1, 2], 2, 1, {'a': 1, 'b': 2}, 4, 'a']
]

TUPLE_TEST_DATA = (1, 2, 3, 4, 'a', 'b', (1, 2, 3), {'a': 1, 'b': 2})
EXPECTED_TUPLE_TEST_DATA = [
    (1, 2, 3, 4, 'a', {'a': 1, 'b': 2}, 'b', (1, 2, 3)),
    (4, 3, {'b': 2, 'a': 1}, 2, 1, 'b', 'a', (3, 2, 1)),
    ('b', (3, 1, 2), 2, 1, {'a': 1, 'b': 2}, 4, 3, 'a')
]
NOT_EXPECTED_TUPLE_TEST_DATA = [
    (9, 1, 2, 3, 4, 'a', {'a': 1, 'b': 2}, 'b', (1, 2, 3)),
    (9, 4, 3, {'b': 2, 'a': 1}, 2, 1, 'b', 'a', (3, 2, 1)),
    (9, 'b', (3, 1, 2), 2, 1, {'a': 1, 'b': 2}, 4, 'a')
]

SET_TEST_DATA = set([1, 2, 3, 4, 'a', 'b', (1, 2, 3)])
EXPECTED_SET_TEST_DATA = [
    set([1, 2, 3, 4, 'a', 'b', (1, 2, 3)]),
    set([4, 3, 2, 1, 'b', 'a', (3, 2, 1)]),
    set(['b', (3, 1, 2), 2, 1, 4, 3, 'a'])
]
NOT_EXPECTED_SET_TEST_DATA = [
    set([9, 1, 2, 3, 4, 'a', 'b', (1, 2, 3)]),
    set([9, 4, 3, 2, 1, 'b', 'a', (3, 2, 1)]),
    set([9, 'b', (3, 1, 2), 2, 1, 4, 'a'])
]

DICT_TEST_DATA = {'a': [1, 2, 3], 'b': {'x': 10, 'y': 20}}
EXPECTED_DICT_TEST_DATA = [
    {'a': [2, 1, 3], 'b': {'y': 20, 'x': 10}},
    {'b': {'x': 10, 'y': 20}, 'a': [2, 1, 3]}
]
NOT_EXPECTED_DICT_TEST_DATA = [
    {'Z': 'W', 'A': [2, 1, 3], 'B': {'Y': 20, 'X': 10}},
    {'Z': 'W', 'B': {'X': 10, 'Y': 20}, 'A': [2, 1, 3]}
]

UUID_TEST_DATA = uuid4()
EXPECTED_UUID_TEST_DATA = [
    UUID_TEST_DATA
]
NOT_EXPECTED_UUID_TEST_DATA = [
    uuid4(),
    uuid4()
]

#-----------------------------------------------------------------------------


def is_expected(item, expected):
    expect(item).to_be_like(expected)


def is_expected_to_fail(item, expected):
    try:
        expect(item).to_be_like(expected)
    except AssertionError:
        return

    assert False, "Shouldn't have gotten this far"


def is_not_expected(item, expected):
    expect(item).Not.to_be_like(expected)
    expect(item).not_to_be_like(expected)

#-----------------------------------------------------------------------------


def test_likeness():
    yield is_expected, None, None

    for expected_item in EXPECTED_STRING_TEST_DATA:
        yield is_expected, STRING_TEST_DATA, expected_item

    for expected_item in EXPECTED_NUMBER_TEST_DATA:
        yield is_expected, NUMBER_TEST_DATA, expected_item
 
    for expected_item in EXPECTED_LIST_TEST_DATA:
        yield is_expected, LIST_TEST_DATA, expected_item

    for expected_item in EXPECTED_TUPLE_TEST_DATA:
        yield is_expected, TUPLE_TEST_DATA, expected_item

    for expected_item in EXPECTED_SET_TEST_DATA:
        yield is_expected, SET_TEST_DATA, expected_item

    for expected_item in EXPECTED_DICT_TEST_DATA:
        yield is_expected, DICT_TEST_DATA, expected_item

    for expected_item in EXPECTED_DATETIME_TEST_DATA:
        yield is_expected, DATETIME_TEST_DATA, expected_item

    for expected_item in EXPECTED_UUID_TEST_DATA:
        yield is_expected, UUID_TEST_DATA, expected_item


def test_likeness_fails():
    yield is_expected, None, None

    for expected_item in NOT_EXPECTED_STRING_TEST_DATA:
        yield is_expected_to_fail, STRING_TEST_DATA, expected_item

    for expected_item in NOT_EXPECTED_NUMBER_TEST_DATA:
        yield is_expected_to_fail, NUMBER_TEST_DATA, expected_item

    for expected_item in NOT_EXPECTED_LIST_TEST_DATA:
        yield is_expected_to_fail, LIST_TEST_DATA, expected_item

    for expected_item in NOT_EXPECTED_TUPLE_TEST_DATA:
        yield is_expected_to_fail, TUPLE_TEST_DATA, expected_item

    for expected_item in NOT_EXPECTED_SET_TEST_DATA:
        yield is_expected_to_fail, SET_TEST_DATA, expected_item

    for expected_item in NOT_EXPECTED_DICT_TEST_DATA:
        yield is_expected_to_fail, DICT_TEST_DATA, expected_item

    for expected_item in NOT_EXPECTED_DATETIME_TEST_DATA:
        yield is_expected_to_fail, DATETIME_TEST_DATA, expected_item

    for expected_item in NOT_EXPECTED_UUID_TEST_DATA:
        yield is_expected_to_fail, UUID_TEST_DATA, expected_item


def test_not_likeness():
    yield is_not_expected, None, 1

    for not_expected_item in NOT_EXPECTED_STRING_TEST_DATA:
        yield is_not_expected, STRING_TEST_DATA, not_expected_item

    for not_expected_item in NOT_EXPECTED_LIST_TEST_DATA:
        yield is_not_expected, LIST_TEST_DATA, not_expected_item

    for not_expected_item in NOT_EXPECTED_TUPLE_TEST_DATA:
        yield is_not_expected, TUPLE_TEST_DATA, not_expected_item

    for not_expected_item in NOT_EXPECTED_SET_TEST_DATA:
        yield is_not_expected, SET_TEST_DATA, not_expected_item

    for not_expected_item in NOT_EXPECTED_DICT_TEST_DATA:
        yield is_not_expected, DICT_TEST_DATA, not_expected_item

    for expected_item in NOT_EXPECTED_DATETIME_TEST_DATA:
        yield is_not_expected, DATETIME_TEST_DATA, expected_item

    for expected_item in NOT_EXPECTED_UUID_TEST_DATA:
        yield is_not_expected, UUID_TEST_DATA, expected_item


def test_likeness_of_objects():
    try:
        expect(object()).to_be_like(1)
    except RuntimeError:
        err = sys.exc_info()[1]
        assert err.__class__ is RuntimeError


def test_likeness_of_different_types():
    expect(1).not_to_be_like('1')
