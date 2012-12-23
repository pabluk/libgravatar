#!/usr/bin/env python3
#
# python-gravatar - Copyright (c) 2009 Pablo Seminario
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

"""
A library that provides a Python 3 interface to the Gravatar XML-RPC API.
"""

__author__ = 'Pablo SEMINARIO <pabluk@gmail.com>'
__version__ = '0.2'

import xmlrpc.client
from hashlib import md5

API_URI = 'https://secure.gravatar.com/xmlrpc?user={0}'


class Gravatar(object):
    """
    This class encapsulates all methods from the API.
    API details: http://en.gravatar.com/site/implement/xmlrpc
    """

    def __init__(self, email, apikey='', password=''):
        self.apikey = apikey
        self.password = password
        self.email = email.lower().strip()
        self.email_hash = md5(email.encode('utf-8')).hexdigest()
        self._server = xmlrpc.client.ServerProxy(API_URI.format(self.email_hash))

    def exists(self, hashes):
        """Checks whether a hash has a gravatar."""
        response = self._call('exists', params={'hashes':hashes})
        results = {}
        for key, value in response.items():
            results[key] = True if value else False
        return results

    def addresses(self):
        """Gets a list of addresses for this account."""
        return self._call('addresses')

    def test(self):
        """Test the API."""
        return self._call('test')

    def _call(self, method, params={}):
        """Call a method from the API, gets 'grav.' prepended to it."""

        args = {
            'apikey': self.apikey,
            'password': self.password,
        }
        args.update(params)

        try:
            return getattr(self._server, 'grav.' + method, None)(args)
        except xmlrpc.client.Fault as error:
            print("Server error: {1} (error code: {0})".format(error.faultCode, error.faultString))


if __name__ == '__main__':
    g = Gravatar('user@example.com', password='12345')
    g.test()
