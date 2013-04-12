#!/usr/bin/env python
# -*- coding: utf-8 -*-

# preggy assertions
# https://github.com/heynemann/preggy

# Licensed under the MIT license:
# http://www.opensource.org/licenses/mit-license
# Copyright (c) 2013 Bernardo Heynemann heynemann@gmail.com

from preggy import expect


def test_to_match():
    expect("a123b").to_match(r"a\d+b")

    try:
        expect("a123b").not_to_match(r"a\d+b")
    except AssertionError:
        return

    assert False, "Should not have gotten this far"


def test_not_to_match():
    expect("b123a").Not.to_match(r"a\d+b")
    expect("b123a").not_to_match(r"a\d+b")

    try:
        expect("b123a").to_match(r"a\d+b")
    except AssertionError:
        return

    assert False, "Should not have gotten this far"
