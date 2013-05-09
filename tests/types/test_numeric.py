# -*- coding: utf-8 -*-

# preggy assertions
# https://github.com/heynemann/preggy

# Licensed under the MIT license:
# http://www.opensource.org/licenses/mit-license
# Copyright (c) 2013 Bernardo Heynemann heynemann@gmail.com

from preggy import expect


TEST_DATA = frozenset([
    10,
    20,
    30.5,
    10 / 3
])


def is_expected(item):
    expect(item).to_be_numeric()


def test_to_be_numeric():
    for item in TEST_DATA:
        yield is_expected, item
