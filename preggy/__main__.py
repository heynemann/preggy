#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function

#import os
#from os import path
#from os.path import (abspath, basename, dirname, join as joinpath)
from textwrap import dedent
import sys

try:
    from colorama import Fore, Style
except ImportError:  
    class _NoColor(object):
        def __getattribute__(self):
            return ''

    Fore = Style = _NoColor()

from preggy import __meta__
from preggy.core import _registered_assertions


#--------------------------------------------------------------------------------
#   Misc Functions
#--------------------------------------------------------------------------------
_longest_of_list= lambda lst: max([len(i) for i in lst])

def _format_module_name(m_name):
    m_formatted = m_name[18:]  # remove "assertions."

    if m_formatted.startswith('types'):
        m_formatted = m_formatted[6:]  # remove "types."

    return m_formatted.capitalize()# + ':'

def _sort_assertion(func):
    name = func.__name__
    if name.startswith('not_to_'):
        return name[7:] + '_z' # ensure that `not_...` comes second
    return name[3:]

def _map_assertions_to_modules(modules=None, assertions=None, sort_func=_sort_assertion):
    '''Returns a dict containing (module:[sorted list of assertions]).'''
    mod_to_assertions = dict.fromkeys(modules)

    for mod in mod_to_assertions.keys():
        _assertions = [f for f in assertions if mod == f.__module__]
        _assertions = sorted(_assertions, key=sort_func)
        mod_to_assertions[mod] = _assertions

    return mod_to_assertions

def _print_assertions():
    #PREGGY_DIR      = dirname(__file__)
    #ASSERTIONS_DIR  = joinpath(PREGGY_DIR, 'assertions')
    
    DIVIDER         = '-' * 55
    DIVIDER         = ''.join((Style.DIM, DIVIDER, Style.RESET_ALL))
    FMT_FIRST_LINE  = '    {colors[module]}{module:<{module_space}}{colors[reset]}{colors[assertion]}{assertions[0]}{colors[reset]}'
    FMT_OTHER_LINES = '    {indent}{colors[assertion]}{name}{colors[reset]}'

    #assertion_names = _registered_assertions.keys()
    assertion_fns   = _registered_assertions.values()

    module_names            = set(i.__module__ for i in assertion_fns)  # remove duplicates
    module_names            = sorted(module_names)
    formatted_module_names  = [_format_module_name(m) for m in module_names]

    #longest_assertion_name  = _longest_of_list(assertion_names)
    longest_module_name     = _longest_of_list(formatted_module_names)

    assertions_by_module    = _map_assertions_to_modules(
        modules=module_names,
        assertions=assertion_fns)

    for modname in module_names:
        module = _format_module_name(modname).upper()

        _assertions = [
            '{indent}{name}'.format(
                name    = f.__name__,
                indent  = '' if (f.__name__.startswith('not')) else 4*' '
            ) for f in assertions_by_module[modname] ]
        
        colors = {
            'module':   Style.DIM,
            'assertion':Style.NORMAL,
            'reset':    Fore.RESET + Style.RESET_ALL,
        }

        print(DIVIDER)
        print(FMT_FIRST_LINE.format(
                module      =module,
                module_space=longest_module_name+4,
                assertions  = _assertions,
                colors      = colors
            ))

        _assertions = [FMT_OTHER_LINES.format(
                            indent  = ' ' * (4+longest_module_name),
                            name    = name,
                            colors  = colors)
                        for name in _assertions
                    ]
        print('\n'.join(_assertions[1:]))

    print(DIVIDER)


#--------------------------------------------------------------------------------
#   The main's mane
#--------------------------------------------------------------------------------
def main():
    print('\n')
    print( Style.BRIGHT, 
         '{0:^55}'.format('Assertions Reference', ).upper(), 
         Style.RESET_ALL, 
        sep='')
    _print_assertions()
    
    INFO_STR = dedent(
    '''
    {0.__name__} {0.__version__} {Style.DIM}({0.__date__:%Y/%m/%d}){Style.RESET_ALL}
    {Fore.RESET}{Style.NORMAL}{0.__url__}{Style.RESET_ALL}{Fore.RESET}
    '''.format(__meta__, Fore=Fore, Style=Style)
    )
    
    print(INFO_STR)
    print('{0.__copyright__}'.format(__meta__), end=2*'\n')
    print('{0.__license_full__}'.format(__meta__), 
            end= 2*'\n')
    

    
if __name__ == '__main__':
    sys.exit(main())
