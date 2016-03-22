# -*- coding: utf-8 -*-

# preggy assertions
# https://github.com/heynemann/preggy

# Licensed under the MIT license:
# http://www.opensource.org/licenses/mit-license
# Copyright (c) 2013 Bernardo Heynemann heynemann@gmail.com

import six
import sys

from preggy import expect


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
        e_values = six.text_type(topic), 'some bogus'
        e_message = e_format.format(*e_values)
        expect(err).to_have_an_error_message_of(e_message)

    try:
        expect(2).to_be_an_error()
    except AssertionError as err:
        expect(err).to_have_an_error_message_of('Expected topic(2) to be an error')


def test_to_be_an_error_like():
    try:
        expect(RuntimeError('Something Wrong')).to_be_an_error_like(ValueError)
    except AssertionError:
        return

    assert False, 'Should not have gotten this far'


def test_not_to_be_an_error_like():
    expect('Something Wrong').Not.to_be_an_error_like(ValueError)


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


def test_can_trap_errors_unicode():
    err = expect.error_to_happen(RuntimeError)

    with err:
        raise RuntimeError(six.u("algo está errado"))

    expect(err).to_have_an_error_message_of(six.u("algo está errado"))

    with expect.error_to_happen(RuntimeError, message=six.u("algo está errado")):
        raise RuntimeError(six.u("algo está errado"))


def test_can_trap_errors_fails_if_error_does_not_happen():
    class_name = "%s.RuntimeError" % RuntimeError.__module__
    err = expect.error_to_happen(RuntimeError)

    try:
        with err:
            pass
    except AssertionError:
        error = sys.exc_info()[1]
        expect(error).to_have_an_error_message_of(
            'Expected "%s" to happen but no errors happened during execution of with block.' % class_name
        )
    else:
        expect.not_to_be_here()

    try:
        with expect.error_to_happen(RuntimeError):
            pass
    except AssertionError:
        error = sys.exc_info()[1]
        expect(error).to_have_an_error_message_of(
            'Expected "%s" to happen but no errors happened during execution of with block.' % class_name
        )
    else:
        expect.not_to_be_here()


def test_can_trap_errors_fails_if_wrong_error():
    class_name = "%s.RuntimeError" % RuntimeError.__module__
    value_class_name = "%s.ValueError" % ValueError.__module__
    err = expect.error_to_happen(RuntimeError)

    try:
        with err:
            raise ValueError("something else entirely")
    except AssertionError:
        error = sys.exc_info()[1]
        expect(error).to_have_an_error_message_of(
            'Expected "%s" to happen but "%s" happened during execution of with block.' % (class_name, value_class_name)
        )
    else:
        expect.not_to_be_here()


def test_can_trap_errors_fails_if_wrong_error_message():
    class_name = "%s.ValueError" % ValueError.__module__
    err = expect.error_to_happen(ValueError, message="Woot?")

    try:
        with err:
            raise ValueError("something else entirely")
    except AssertionError:
        error = sys.exc_info()[1]
        expect(error).to_have_an_error_message_of(
            'Expected "%s" to have a message of "Woot?", but the actual error was "something else entirely".' % class_name
        )
    else:
        expect.not_to_be_here()


def test_can_NOT_trap_errors():
    try:
        with expect.not_error_to_happen(RuntimeError):
            raise RuntimeError("something is wrong")
    except AssertionError, err:
        expect(str(err)).to_equal(
            'Expected "exceptions.RuntimeError" not to happen but it happened during execution of with block.'
        )
        return

    expect.not_to_be_here()


def test_can_trap_errors_but_fail_due_to_type():
    try:
        with expect.not_error_to_happen(RuntimeError):
            raise ValueError("something is wrong")
    except AssertionError, err:
        expect(str(err)).to_equal(
            'Expected "exceptions.RuntimeError" not to happen but '
            '"exceptions.ValueError" happened during execution of with block.'
        )
        return

    expect.not_to_be_here()


def test_can_trap_errors_but_fail_due_to_message():
    try:
        with expect.not_error_to_happen(RuntimeError, message="qweqwe"):
            raise RuntimeError("something is wrong")
    except AssertionError, err:
        expect(str(err)).to_equal(
            'Expected "exceptions.RuntimeError" to have a message of "qweqwe", but the actual error was "something is wrong".'
        )
        return

    expect.not_to_be_here()


