# -*- coding: utf-8 -*-

# preggy assertions
# https://github.com/heynemann/preggy

# Licensed under the MIT license:
# http://www.opensource.org/licenses/mit-license
# Copyright (c) 2013 Bernardo Heynemann heynemann@gmail.com

from preggy import expect

import pytest

#-----------------------------------------------------------------------------

EMPTY_DATA = (
    '',
    [],
    {},
    tuple([])
)

NOT_EMPTY_DATA = (
    'qwe',
    [1],
    {'a': 'b'},
    tuple([2])
)

#-----------------------------------------------------------------------------

def is_empty(item):
    expect(item).to_be_empty()


def is_not_empty(item):
    expect(item).Not.to_be_empty()
    expect(item).not_to_be_empty()

#-----------------------------------------------------------------------------

@pytest.mark.parametrize("item", EMPTY_DATA)
def test_emptiness_assertion_works(item):
    is_empty(item)


@pytest.mark.parametrize("item", NOT_EMPTY_DATA)
def test_not_emptiness_assertion_works(item):
    is_not_empty(item)
