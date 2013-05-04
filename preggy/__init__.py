# -*- coding: utf-8 -*-

# preggy assertions
# https://github.com/heynemann/preggy

# Licensed under the MIT license:
# http://www.opensource.org/licenses/mit-license
# Copyright (c) 2013 Bernardo Heynemann heynemann@gmail.com

# flake8: noqa

from __future__ import absolute_import

__version__ = "0.3.12"

from preggy.core import Assertions
assertion = Assertions.assertion
create_assertions = Assertions.create_assertions

from preggy.core import Expect as expect
from preggy.assertions import *