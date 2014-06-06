# -*- coding: utf-8 -*-

# preggy assertions
# https://github.com/heynemann/preggy

# Licensed under the MIT license:
# http://www.opensource.org/licenses/mit-license
# Copyright (c) 2013 Bernardo Heynemann heynemann@gmail.com

import six
import sys

from preggy import expect

#-----------------------------------------------------------------------------



def test_is_error():
    topic = RuntimeError('Something Wrong') 
    expect(topic).to_be_an_error()
    expect(topic).to_be_an_error_like(RuntimeError)
    expect(topic).to_have_an_error_message_of('Something Wrong')
    
    topic = ValueError('some bogus error')
    expect(topic).to_be_an_error()
    expect(topic).to_be_an_error_like(ValueError)
    expect(topic).to_have_an_error_message_of('some bogus error')


def test_not_to_be_an_error():
    NON_ERRORS = frozenset([
        0,
        2,
        tuple(),
        object(),
        'b123a',
        r'b123a',
        six.u('b123a'),
        b'b123a'
    ])
    
    for item in NON_ERRORS:
        expect(item).Not.to_be_an_error()
        expect(item).not_to_be_an_error()
        
        # try:
        #     expect(item).to_be_an_error()
        # except AssertionError as err:
        #     expect(err).to_have_an_error_message_of("Expected topic({0}) to be an error".format(item))
            


def test_error_messages():
    topic = Exception('1 does not equal 2')
    expect(topic).to_have_an_error_message_of('1 does not equal 2')
    
    try:
        expect(topic).to_have_an_error_message_of('some bogus')
    except AssertionError as err:
        e_format = "Expected topic({0!r}) to be an error with message {1!r}"
        e_values = str(topic), 'some bogus'
        e_message = e_format.format(*e_values)
        expect(err).to_have_an_error_message_of(e_message)
    
    try:
        expect(2).to_be_an_error()
    except AssertionError as err:
        expect(err).to_have_an_error_message_of('Expected topic(2) to be an error')
    

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

def test_can_trap_errors():
    err = expect.error_to_happen(RuntimeError)

    with err:
        raise RuntimeError("something is wrong")

    expect(err).to_have_an_error_message_of('something is wrong')

    with expect.error_to_happen(RuntimeError, message="something is wrong"):
        raise RuntimeError("something is wrong")

def test_can_trap_errors_fails_if_error_does_not_happen():
    err = expect.error_to_happen(RuntimeError)

    try:
        with err:
            pass
    except AssertionError:
        error = sys.exc_info()[1]
        expect(error).to_have_an_error_message_of('Expected "exceptions.RuntimeError" to happen but no errors happened during execution of with block.')
    else:
        expect.not_to_be_here()

    try:
        with expect.error_to_happen(RuntimeError):
            pass
    except AssertionError:
        error = sys.exc_info()[1]
        expect(error).to_have_an_error_message_of('Expected "exceptions.RuntimeError" to happen but no errors happened during execution of with block.')
    else:
        expect.not_to_be_here()


def test_can_trap_errors_fails_if_wrong_error():
    err = expect.error_to_happen(RuntimeError)

    try:
        with err:
            raise ValueError("something else entirely")
    except AssertionError:
        error = sys.exc_info()[1]
        expect(error).to_have_an_error_message_of('Expected "exceptions.RuntimeError" to happen but "exceptions.ValueError" happened during execution of with block.')
    else:
        expect.not_to_be_here()
