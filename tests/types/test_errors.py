# -*- coding: utf-8 -*-

# preggy assertions
# https://github.com/heynemann/preggy

# Licensed under the MIT license:
# http://www.opensource.org/licenses/mit-license
# Copyright (c) 2013 Bernardo Heynemann heynemann@gmail.com

from preggy import expect

#-----------------------------------------------------------------------------

def test_is_error():
    expect(RuntimeError()).to_be_an_error()
    expect(RuntimeError('Something Wrong')).to_be_an_error_like(RuntimeError)
    expect(RuntimeError('Something Wrong')).to_have_an_error_message_of('Something Wrong')


def test_not_to_be_an_error():
    expect('b123a').Not.to_be_an_error()
    expect('b123a').not_to_be_an_error()


def test_not_to_be_an_error_like():
    try:
        expect(RuntimeError('Something Wrong')).to_be_an_error_like(ValueError)
    except AssertionError:
        return

    assert False, 'Should not have gotten this far'


def test_not_to_have_error_message():
    try:
        expect(RuntimeError('Something Wrong')).to_have_an_error_message_of('Something Else')
    except AssertionError:
        return

    assert False, 'Should not have gotten this far'
