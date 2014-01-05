# -*- coding: utf-8 -*-
'''All metadata not related to the installation process.'''


# preggy assertions
# https://github.com/heynemann/preggy

# Licensed under the MIT license:
# http://www.opensource.org/licenses/mit-license
# Copyright (c) 2013 Bernardo Heynemann heynemann@gmail.com

# flake8: noqa

from datetime import date


#--------------------------------------------------------------------------------
#   GENERAL
#--------------------------------------------------------------------------------
__name__        = 'preggy'  # normally preggy.__meta__
__version__     = '0.9.0'
__date__        = date(2014, 1, 5)  # TODO: auto-populate each release using a git hook
__keywords__    = 'test testing assert assertion library development'
__status__      = 'Production'


#--------------------------------------------------------------------------------
#   URLS
#--------------------------------------------------------------------------------
__url__         = 'http://heynemann.github.io/preggy'
__download_url__= 'https://github.com/heynemann/preggy/releases/tag/{version}'.format(version=__version__)
__bugtrack_url__= 'http://github.com/heynemann/preggy/issues'


#--------------------------------------------------------------------------------
#   PEOPLE
#--------------------------------------------------------------------------------
__author__      = 'Bernardo Heynemann'
__author_email__= 'heynemann@gmail.com'

__maintainer__      = 'Zearin'
__maintainer_email__= 'zearin@gonk.net'

__credits__     = (__author__, __maintainer__,)


#--------------------------------------------------------------------------------
#   LEGAL
#--------------------------------------------------------------------------------
__copyright__   = 'Copyright (c) 2013 {author} <{email}>'.format(
    author=__author__,
    email=__author_email__)

__license__     = 'MIT'
__license_full__= '''
Licensed under the MIT license:
http://www.opensource.org/licenses/mit-license
'''.strip()

