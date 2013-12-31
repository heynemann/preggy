# -*- coding: utf-8 -*-
'''Assorted helpers used elsewhere in preggy.  

Currently contains only string formatting code, but this may (or may not) change.
'''
# preggy assertions
# https://github.com/heynemann/preggy

# Licensed under the MIT license:
# http://www.opensource.org/licenses/mit-license
# Copyright (c) 2013 Bernardo Heynemann heynemann@gmail.com

from __future__ import absolute_import
import re

try:
    import six
except ImportError:  # pragma: no cover
    import warnings
    warnings.warn('Ignoring six. Probably setup.py installing package.')

try:
    from unidecode import unidecode
except ImportError:  # pragma: no cover
    import warnings
    warnings.warn('Ignoring unidecode. Probably setup.py installing package.')


humanized_name = lambda x: re.sub(r'_+', ' ', x.__name__)

def fix_string(obj):
    if isinstance(obj, (six.binary_type, )):
        try:
            return obj.decode('utf-8')
        except Exception:
            return unidecode(obj)
    return obj
