# -*- coding: utf-8 -*-

# preggy assertions
# https://github.com/heynemann/preggy

# Licensed under the MIT license:
# http://www.opensource.org/licenses/mit-license
# Copyright (c) 2013 Bernardo Heynemann heynemann@gmail.com

import sys
from preggy import expect

#-----------------------------------------------------------------------------

def test_expect_not_to_be_here():
    try:
        expect.not_to_be_here()
    except AssertionError:
        err = sys.exc_info()[1]
        expect(err).to_be_an_error()
        expect(err).to_be_an_error_like(AssertionError)
        expect(err).to_have_an_error_message_of("Should not have gotten this far.")
    else:
        assert False, "Should not have gotten this far."
