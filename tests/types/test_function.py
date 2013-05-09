# -*- coding: utf-8 -*-

# preggy assertions
# https://github.com/heynemann/preggy

# Licensed under the MIT license:
# http://www.opensource.org/licenses/mit-license
# Copyright (c) 2013 Bernardo Heynemann heynemann@gmail.com

from preggy import expect

#-----------------------------------------------------------------------------

def fake_method(): 
    pass
class FakeClass(object):
    def whatever(self): 
        pass

TEST_DATA = frozenset([
    fake_method,
    FakeClass.whatever,
    FakeClass().whatever
])

#-----------------------------------------------------------------------------

def is_expected(item):
    expect(item).to_be_a_function()
    try:
        expect(item).not_to_be_a_function()
    except AssertionError:
        return
    assert False, "Should not have gotten this far"


def is_not_expected(item):
    expect(item).Not.to_be_a_function()
    expect(item).not_to_be_a_function()

    try:
        expect(item).to_be_a_function()
    except AssertionError:
        return
    assert False, "Should not have gotten this far"

#-----------------------------------------------------------------------------

def test_to_be_a_function():
    for item in TEST_DATA:
        yield is_expected, item


def test_not_to_be_a_function():
    is_not_expected("a")
    is_not_expected((1, 2))
    is_not_expected([1, 2])
