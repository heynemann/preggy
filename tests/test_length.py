#!/usr/bin/env python
# -*- coding: utf-8 -*-

# preggy assertions
# https://github.com/heynemann/preggy

# Licensed under the MIT license:
# http://www.opensource.org/licenses/mit-license
# Copyright (c) 2013 Bernardo Heynemann heynemann@gmail.com

from preggy import expect


TEST_DATA = [
    "12345",
    [1, 2, 3],
    {"a": 1, "b": 2},
    tuple([1, 2, 3, 4, 5, 6])
]

EXPECTED_DATA = [
    5,
    3,
    2,
    6
]

NOT_EXPECTED_DATA = [
    7,
    2,
    3,
    5
]


def is_expected(item, expected):
    expect(item).to_length(expected)


def is_not_expected(item, expected):
    expect(item).Not.to_length(expected)
    expect(item).not_to_length(expected)


def test_length():
    for index, item in enumerate(TEST_DATA):
        yield is_expected, item, EXPECTED_DATA[index]


def test_not_includes():
    for index, item in enumerate(TEST_DATA):
        yield is_not_expected, item, NOT_EXPECTED_DATA[index]
