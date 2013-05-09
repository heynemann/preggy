# -*- coding: utf-8 -*-

# preggy assertions
# https://github.com/heynemann/preggy

# Licensed under the MIT license:
# http://www.opensource.org/licenses/mit-license
# Copyright (c) 2013 Bernardo Heynemann heynemann@gmail.com

from preggy import expect

#-----------------------------------------------------------------------------

TEST_DATA = frozenset([
    './README.md',
])

FAIL_DATA = frozenset([
    './READM.md',
    0,
    (1, 2, 3)
])

#-----------------------------------------------------------------------------

def is_expected(item):
    with open(item) as f:
        expect(f).to_be_a_file()
        expect(item).to_be_a_file()
        try:
            expect(item).not_to_be_a_file()
        except AssertionError:
            return
        assert False, 'Should not have gotten this far'


def is_not_expected(item):
    expect(item).Not.to_be_a_file()
    expect(item).not_to_be_a_file()

    try:
        expect(item).to_be_a_file()
    except AssertionError:
        return

    assert False, 'Should not have gotten this far'

#-----------------------------------------------------------------------------

def test_to_be_a_file():
    for item in TEST_DATA:
        yield is_expected, item


def test_not_to_be_a_file():
    for item in FAIL_DATA:
        yield is_not_expected, item


def test_is_not_file_obj():
    with open('./README.md') as f:
        try:
            expect(f).not_to_be_a_file()
        except AssertionError:
            return

        assert False, 'Should not have gotten this far'
