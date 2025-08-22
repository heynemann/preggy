# -*- coding: utf-8 -*-

# preggy assertions
# https://github.com/heynemann/preggy

# Licensed under the MIT license:
# http://www.opensource.org/licenses/mit-license
# Copyright (c) 2013 Bernardo Heynemann heynemann@gmail.com

import sys
from datetime import datetime
from uuid import uuid4

import pytest

from preggy import expect

from tests import Comparable, AnotherComparable

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

CMP_LIST_TEST_DATA = [AnotherComparable('X'), Comparable('Y'), Comparable('Z')]
EXPECTED_CMP_LIST_TEST_DATA = [
    [Comparable('Z'), Comparable('Y'), AnotherComparable('X')],
    [Comparable('Y'), Comparable('Z'), AnotherComparable('X')],
    [Comparable('Z'), AnotherComparable('X'), Comparable('Y')]
]
NOT_EXPECTED_CMP_LIST_TEST_DATA = [
    [Comparable('A'), Comparable('B'), Comparable('C')],
    [AnotherComparable('Z'), Comparable('Y'), AnotherComparable('X')],
    [Comparable('Y'), AnotherComparable('Z'), AnotherComparable('X')],
    [AnotherComparable('Z'), AnotherComparable('X'), Comparable('Y')]
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

CMP_DICT_TEST_DATA = {
    'a': Comparable('X'),
    'b': {'J': AnotherComparable('J'), 'K': 'K', 'L': Comparable('L')},
    'c': [1, 2, 3, Comparable('4')]
}
EXPECTED_CMP_DICT_TEST_DATA = [{
    'b': {'K': 'K', 'L': Comparable('L'), 'J': AnotherComparable('J'), },
    'c': [3, Comparable('4'), 1, 2],
    'a': Comparable('X')
}, {
    'c': [Comparable('4'), 3, 2, 1],
    'a': Comparable('X'),
    'b': {'L': Comparable('L'), 'J': AnotherComparable('J'), 'K': 'K'}
}]
NOT_EXPECTED_CMP_DICT_TEST_DATA = [{
    'a': Comparable('x'),
    'b': {'J': AnotherComparable('j'), 'K': 'k', 'L': Comparable('l')},
    'c': [5, 6, 7, Comparable('8')]
}, {
    'a': AnotherComparable('X'),
    'b': {'K': AnotherComparable('K'), 'L': 'L', 'J': Comparable('J')},
    'c': [Comparable('1'), Comparable('2'), Comparable('3'), 4]
}]

UUID_TEST_DATA = uuid4()
EXPECTED_UUID_TEST_DATA = [
    UUID_TEST_DATA
]
NOT_EXPECTED_UUID_TEST_DATA = [
    uuid4(),
    uuid4()
]

CMPCLASS_TEST_DATA = Comparable('preggy')
EXPECTED_CMPCLASS_TEST_DATA = [
    Comparable('preggy')
]
NOT_EXPECTED_CMPCLASS_TEST_DATA = [
    Comparable('PREGGY'),
    AnotherComparable('preggy')
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


def pytest_generate_tests(metafunc):
    if 'expected' in metafunc.fixturenames:
        if 'item' in metafunc.fixturenames:
            parameter = "item, expected"
            data_list = (
                (STRING_TEST_DATA, EXPECTED_STRING_TEST_DATA),
                (LIST_TEST_DATA, EXPECTED_LIST_TEST_DATA),
                (CMP_LIST_TEST_DATA, EXPECTED_CMP_LIST_TEST_DATA),
                (TUPLE_TEST_DATA, EXPECTED_TUPLE_TEST_DATA),
                (SET_TEST_DATA, EXPECTED_SET_TEST_DATA),
                (DICT_TEST_DATA, EXPECTED_DICT_TEST_DATA),
                (CMP_DICT_TEST_DATA, EXPECTED_CMP_DICT_TEST_DATA),
                (DATETIME_TEST_DATA, EXPECTED_DATETIME_TEST_DATA),
                (UUID_TEST_DATA, EXPECTED_UUID_TEST_DATA),
                (CMPCLASS_TEST_DATA, EXPECTED_CMPCLASS_TEST_DATA))
        elif 'not_item' in metafunc.fixturenames:
            parameter = "not_item, expected"
            data_list = (
                (STRING_TEST_DATA, NOT_EXPECTED_STRING_TEST_DATA),
                (LIST_TEST_DATA, NOT_EXPECTED_LIST_TEST_DATA),
                (CMP_LIST_TEST_DATA, NOT_EXPECTED_CMP_LIST_TEST_DATA),
                (TUPLE_TEST_DATA, NOT_EXPECTED_TUPLE_TEST_DATA),
                (SET_TEST_DATA, NOT_EXPECTED_SET_TEST_DATA),
                (DICT_TEST_DATA, NOT_EXPECTED_DICT_TEST_DATA),
                (CMP_DICT_TEST_DATA, NOT_EXPECTED_CMP_DICT_TEST_DATA),
                (DATETIME_TEST_DATA, NOT_EXPECTED_DATETIME_TEST_DATA),
                (UUID_TEST_DATA, NOT_EXPECTED_UUID_TEST_DATA),
                (CMPCLASS_TEST_DATA, NOT_EXPECTED_CMPCLASS_TEST_DATA))
        data = []
        for expected, items in data_list:
            for item in items:
                data.append((item, expected))
        metafunc.parametrize(parameter, data)


def test_likeness():
    is_expected(None, None)


def test_likeness_data(item, expected):
    is_expected(item, expected)


def test_likeness_fails():
    is_expected_to_fail(None, 1)


def test_likeness_fails_data(not_item, expected):
    is_expected_to_fail(not_item, expected)


def test_not_likeness():
    is_not_expected(None, 1)


def test_not_likeness_test_data(not_item, expected):
    is_not_expected(not_item, expected)


def test_likeness_of_objects():
    try:
        expect(object()).to_be_like(1)
    except RuntimeError:
        err = sys.exc_info()[1]
        assert err.__class__ is RuntimeError


def test_likeness_of_different_types():
    expect(1).not_to_be_like('1')
