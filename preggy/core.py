# -*- coding: utf-8 -*-
'''preggy core: the `Expect` class, and the `@assertion` and `@create_assertions` decorators.
'''
# preggy assertions
# https://github.com/heynemann/preggy

# Licensed under the MIT license:
# http://www.opensource.org/licenses/mit-license
# Copyright (c) 2013 Bernardo Heynemann heynemann@gmail.com

from __future__ import absolute_import
import re

_registered_assertions = dict()

def assertion(func):
    '''Function decorator.  Provides lower-level control for custom
    assertions than `@preggy.create_assertions`.

    This decorator is preferable over `@preggy.create_assertions` 
    if you need to fine-tune your error message, or if your assertion 
    doesn’t have a corresponding `not_`. 
    
    Unlike `@preggy.create_assertions`, functions decorated with
    this shouldn’t return a boolean. Instead, they should check for 
    undesirable conditions and raise an `AssertionError` when appropriate. 

    Whenever possible, you should declare both the normal assertion as well
    as a `not_` counterpart, so they can be used like this:

        expect(5).to_be_a_positive_integer()
        expect(-3).Not.to_be_a_positive_integer()
        
    '''
    def func_name(*args, **kw):
        func(*args, **kw)

    def test_assertion(*args, **kw):
        return func_name(*args, **kw)

    _registered_assertions[func.__name__] = test_assertion
    return func_name


def create_assertions(func):
    '''Function decorator.  Use to create custom assertions for your
    tests.
    ''' '''
    Creating new assertions for use with `expect` is as simple as using
    this decorator on a function. The function expects `topic` as the
    first parameter, and `expectation` second:

        @preggy.create_assertions
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
    humanized_name = re.sub(r'_+', ' ', func.__name__)

    def _assertion_msg(assertion_clause, *args):
        raw_msg = 'Expected topic({{0!r}}) {assertion_clause}'.format(
            assertion_clause=assertion_clause)
        if len(args) is 2:
            raw_msg += ' {1!r}'
        return raw_msg

    def test_assertion(*args):
        raw_msg = _assertion_msg(humanized_name, *args)
        if not func(*args):
            raise AssertionError(raw_msg.format(*args))

    def test_not_assertion(*args):
        raw_msg = _assertion_msg('not {0}'.format(humanized_name), *args)
        if func(*args):
            raise AssertionError(raw_msg.format(*args))

    _registered_assertions[func.__name__] = test_assertion
    _registered_assertions['not_{method_name}'.format(method_name=func.__name__)] = test_not_assertion

    def wrapper(*args, **kw):
        return func(*args, **kw)

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
        # common cases
        if name == 'topic':
            return super(Expect, self).__getattr__(name)
        if name == 'Not':
            self.not_assert = not self.not_assert
            return self
        
        # determine whether assertion is of "not" form
        method_name = 'not_{name}'.format(name=name) if self.not_assert  else name

        # check for unregistered assertions
        if method_name not in _registered_assertions:
            raise AttributeError('Assertion "{method_name}" was not found!'.format(method_name=method_name))

        # if program gets this far, then it’s time to perform the assertion. (...FINALLY! ;D)
        def assert_topic(*args, **kw):
            '''Allows chained calls to `Assertion`s.  For example, in:
                
                expect(topic).to_be_true()
            
            This method is what allows `expect(topic)` to call `.to_be_true()`.

            '''
            return _registered_assertions[method_name](self.topic, *args, **kw)

        return assert_topic
