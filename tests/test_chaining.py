# -*- coding: utf-8 -*-

# preggy assertions
# https://github.com/heynemann/preggy

# Licensed under the MIT license:
# http://www.opensource.org/licenses/mit-license
# Copyright (c) 2014 Pablo Santiago Blum de Aguiar <scorphus@gmail.com>

from preggy import expect


def test_chaining():
    expect('qwe') \
        .not_to_be_null() \
        .to_be_instance_of(str) \
        .to_be_like('QWE') \
        .to_equal('qwe')
    expect(1729) \
        .not_to_be_null() \
        .to_be_instance_of(int) \
        .to_be_numeric() \
        .to_be_greater_or_equal_to(496) \
        .to_equal(1729)
    expect(3.14159265358979) \
        .not_to_be_null() \
        .to_be_instance_of(float) \
        .to_be_numeric() \
        .to_be_lesser_or_equal_to(3.1416) \
        .to_be_like(3.14159265358979)
    expect([1, 2, 3]) \
        .not_to_be_null() \
        .not_to_be_empty() \
        .to_be_instance_of(list) \
        .to_be_like([3, 2, 1])
    expect({'a': 'b', 'x': 'z'}) \
        .not_to_be_null() \
        .not_to_be_empty() \
        .to_be_instance_of(dict) \
        .to_be_like({'x': 'z', 'a': 'b'})

    meaning = {'x': 42}
    of_life = {'x': 42}

    expect(meaning.get('y')).to_equal(of_life.get('y'))
    expect(meaning.get('x')).not_to_be_null().to_equal(of_life.get('x'))
    try:
        expect(meaning.get('y')).not_to_be_null().to_equal(of_life.get('x'))
    except AssertionError:
        return
    else:
        assert False, 'Should not have gotten this far'
