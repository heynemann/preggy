# -*- coding: utf-8 -*-

# preggy assertions
# https://github.com/heynemann/preggy

# Licensed under the MIT license:
# http://www.opensource.org/licenses/mit-license
# Copyright (c) 2013 Bernardo Heynemann heynemann@gmail.com

import pytest

from preggy import expect

#-----------------------------------------------------------------------------

TEST_DATA = frozenset([
    10,
    20,
    30.5,
    10 / 3
])

#-----------------------------------------------------------------------------

def is_expected(item):
    expect(item).to_be_numeric()

#-----------------------------------------------------------------------------

@pytest.mark.parametrize("item", TEST_DATA)
def test_to_be_numeric(item):
    is_expected(item)
