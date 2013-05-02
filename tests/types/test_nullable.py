# -*- coding: utf-8 -*-

# preggy assertions
# https://github.com/heynemann/preggy

# Licensed under the MIT license:
# http://www.opensource.org/licenses/mit-license
# Copyright (c) 2013 Bernardo Heynemann heynemann@gmail.com

from preggy import expect


def test_to_be_null():
    expect(None).to_be_null()

    try:
        expect(None).not_to_be_null()
    except AssertionError:
        return

    assert False, "Should not have gotten this far"


def test_not_to_be_null():
    expect("something").Not.to_be_null()
    expect("something").not_to_be_null()

    try:
        expect("something").to_be_null()
    except AssertionError:
        return

    assert False, "Should not have gotten this far"
