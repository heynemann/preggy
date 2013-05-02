# -*- coding: utf-8 -*-

# preggy assertions
# https://github.com/heynemann/preggy

# Licensed under the MIT license:
# http://www.opensource.org/licenses/mit-license
# Copyright (c) 2013 Bernardo Heynemann heynemann@gmail.com

from preggy import expect


class FakeClass(object):
    pass


class Other(FakeClass):
    pass


TEST_DATA = [
    FakeClass,
    FakeClass(),
    Other,
    Other()
]


def is_expected(item):
    expect(item).to_be_instance_of(FakeClass)
    try:
        expect(item).not_to_be_instance_of(FakeClass)
    except AssertionError:
        return
    assert False, "Should not have gotten this far"


def is_not_expected(item):
    expect(item).Not.to_be_instance_of(dict)
    expect(item).not_to_be_instance_of(dict)

    try:
        expect(item).to_be_instance_of(dict)
    except AssertionError:
        return
    assert False, "Should not have gotten this far"


def test_to_be_instance_of():
    for item in TEST_DATA:
        yield is_expected, item


def test_not_to_be_instance_of():
    for item in TEST_DATA:
        yield is_not_expected, item
