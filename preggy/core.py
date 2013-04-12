#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''preggy core assertion class.
'''
# preggy assertions
# https://github.com/heynemann/preggy

# Licensed under the MIT license:
# http://www.opensource.org/licenses/mit-license
# Copyright (c) 2013 Bernardo Heynemann heynemann@gmail.com

import re


class Assertions:
    registered_assertions = {}

    @classmethod
    def assertion(cls, method):
        '''Function decorator.  Provides lower-level control for custom
        assertions than `@Assertions.create_assertions`.

        If you need more control over your error message, or your assertion
        doesn’t have a corresponding `not_`, use this decorator and
        raise a `AssertionError`.

        By raising a `AssertionError`, you get the benefit of highlighting
        the important values when your vows are broken.

        If you still just wanna raise an `AssertionError` like old times,
        that’s supported, too.

        It’s recommended to always declare both the assertion and the `not_`
        assertion (if applicable), so they can be used like this:

            expect(5).to_be_a_positive_integer()
            expect(-3).Not.to_be_a_positive_integer()
        '''
        def method_name(*args, **kw):
            method(*args, **kw)

        def exec_assertion(*args, **kw):
            return method_name(*args, **kw)

        Assertions.registered_assertions[method.__name__] = exec_assertion

        return method_name

    @classmethod
    def create_assertions(cls, method):
        '''Function decorator.  Use to create custom assertions for your
        tests.
        ''' '''
        Creating new assertions for use with `expect` is as simple as using
        this decorator on a function. The function expects `topic` as the
        first parameter, and `expectation` second:

            @Assertions.create_assertions
            def to_be_greater_than(topic, expected):
                return topic > expected

        Now, the following expectation…

            expect(2).to_be_greater_than(3)

        …will report:

            Expected topic(2) to be greater than 3.

        It will also create the corresponding `not_` assertion:

            expect(4).not_to_be_greater_than(3);

        …will report:

            Expected topic(4) not to be greater than 3.
        '''
        humanized_method_name = re.sub(r'_+', ' ', method.__name__)

        def _assertion_msg(assertion_clause=None, *args):
            raw_msg = 'Expected topic({{0}}) {assertion_clause}'.format(
                assertion_clause=assertion_clause)
            if len(args) is 2:
                raw_msg += ' {1}'
            return raw_msg

        def exec_assertion(*args):
            raw_msg = _assertion_msg(humanized_method_name, *args)
            if not method(*args):
                raise AssertionError(raw_msg, *args)

        def exec_not_assertion(*args):
            raw_msg = _assertion_msg('not {0}'.format(humanized_method_name), *args)
            if method(*args):
                raise AssertionError(raw_msg, *args)

        Assertions.registered_assertions[method.__name__] = exec_assertion
        Assertions.registered_assertions['not_{method_name}'.format(method_name=method.__name__)] = exec_not_assertion

        def wrapper(*args, **kw):
            return method(*args, **kw)

        return wrapper


class Expect(object):
    '''This atypical class provides a key part of the preggy testing syntax.

    For example:

        expect(True).to_be_true()

    '''

    def __init__(self, topic):
        self.topic = topic
        self.not_assert = False

    def __getattr__(self, name):
        if name == 'topic':
            return super(Expect, self).__getattr__(name)

        if name == 'Not':
            self.not_assert = not self.not_assert
            return self

        if self.not_assert:
            method_name = 'not_{name}'.format(name=name)
        else:
            method_name = name

        if not method_name in Assertions.registered_assertions:
            raise AttributeError('Assertion {method_name} was not found!'.format(method_name=method_name))

        def assert_topic(*args, **kw):
            '''Allows instances (topics) to chain calls to `Assertion`s.

            In the following preggy-test snippet:

                expect(topic).to_be_True()

            ...This method is what allows `expect(topic)` to call
            `.to_be_True()` (or some other VowsAssertion).

            '''
            return Assertions.registered_assertions[method_name](self.topic, *args, **kw)

        return assert_topic
