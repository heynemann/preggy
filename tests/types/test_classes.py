# -*- coding: utf-8 -*-

# preggy assertions
# https://github.com/heynemann/preggy

# Licensed under the MIT license:
# http://www.opensource.org/licenses/mit-license
# Copyright (c) 2013 Bernardo Heynemann heynemann@gmail.com

import pytest

from preggy import expect

from tests import Comparable

#-----------------------------------------------------------------------------

class FakeClass(object): pass
class Other(FakeClass):  pass
class Another(FakeClass, Comparable): pass

TEST_DATA = frozenset([
    FakeClass,
    FakeClass(),
    Other,
    Other(),
    Another,
    Another()
])

#-----------------------------------------------------------------------------

def is_expected(item):
    expect(item).to_be_instance_of(FakeClass)
    try:
        expect(item).not_to_be_instance_of(FakeClass)
    except AssertionError:
        return
    assert False, 'Should not have gotten this far'


def is_not_expected(item):
    expect(item).Not.to_be_instance_of(dict)
    expect(item).not_to_be_instance_of(dict)

    try:
        expect(item).to_be_instance_of(dict)
    except AssertionError:
        return
    assert False, 'Should not have gotten this far'

#-----------------------------------------------------------------------------

@pytest.mark.parametrize("item", TEST_DATA)
def test_to_be_instance_of(item):
    is_expected(item)


@pytest.mark.parametrize("item", TEST_DATA)
def test_not_to_be_instance_of(item):
    is_not_expected(item)
