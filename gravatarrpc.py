#!/usr/bin/env python
#
# gravatar-rpc - Copyright (c) 2009 Pablo Seminario
# This software is distributed under the terms of the GNU General
# Public License
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

'''A library that provides a python interface to the Gravatar XMLRPC API'''

__author__ = 'pabluk@gmail.com'
__version__ = '0.1'

import xmlrpclib
from hashlib import md5

API_URI = 'https://secure.gravatar.com/xmlrpc?user={0}'

class gravatarrpc:
    '''This class encapsulates all methods from the API
    Usage:
    If you have an account at Wordpress.com you can use your API Key
        gravatar = gravatarrpc('user@domain', apikey='1234')
        gravatar.test() # test the API

    Or you can use your Gravatar.com password
        gravatar = gravatarrpc('user@domain', password='1234')
        gravatar.test() # test the API
    '''

    def __init__(self, email, apikey='', password=''):
       self.apikey = apikey
       self.password = password
       self.email = str.lower(str.strip(email))
       self.params = {}
       self._instance = None

    def _client(self):
        if self._instance is None:
            self._instance = xmlrpclib.ServerProxy(API_URI.format(md5(self.email).hexdigest()))
        return self._instance

    def _call(self, method, params={}):
        '''Call a method from the API, gets 'grav.' prepended to it.'''

        self.params = params
        self.params['apikey'] = self.apikey
        self.params['password'] = self.password

        return getattr(self._client(), 'grav.' + method, None)(params)

    def test(self):
        '''Test the API.'''
        return self._call('test')

    def userimages(self):
        '''Return an array of userimages with your rating and url for this account.'''
        return self._call('userimages')

