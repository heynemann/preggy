# -*- coding: utf-8 -*-

# preggy assertions
# https://github.com/heynemann/preggy

# Licensed under the MIT license:
# http://www.opensource.org/licenses/mit-license
# Copyright (c) 2013 Bernardo Heynemann heynemann@gmail.com

# flake8: noqa

__version__ = "0.3.8"

from preggy.core import Assertions
create_assertions = Assertions.create_assertions
assertion = Assertions.assertion

from preggy.core import Expect as expect

from preggy.emptiness import *
from preggy.equality import *
from preggy.inclusion import *
from preggy.length import *
from preggy.like import *

from preggy.types.numeric import *
from preggy.types.function import *
from preggy.types.boolean import *
from preggy.types.classes import *
from preggy.types.file import *
from preggy.types.nullable import *
from preggy.types.regexp import *
from preggy.types.errors import *
