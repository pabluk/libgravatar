# libgravatar - Copyright (c) 2009 Pablo SEMINARIO
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
A library that provides a Python 3 interface to the Gravatar APIs.
"""

__author__ = 'Pablo SEMINARIO <pabluk@gmail.com>'
__version__ = '0.2.4'

import sys

if sys.version_info[0] < 3:
    # Python 2.x
    from xmlrpclib import ServerProxy, Fault
    from urlparse import urlparse
    from urllib import urlencode
else:
    # Python 3.x
    from xmlrpc.client import ServerProxy, Fault
    from urllib.parse import urlparse, urlencode

from hashlib import md5


class Gravatar(object):
    """
    This class encapsulates all the unauthenticated methods from the API.
    """

    DEFAULT_IMAGE_SIZE = 80
    DEFAULT_IMAGE = [
        '404',
        'mm',
        'mp',
        'identicon',
        'monsterid',
        'wavatar',
        'retro',
        'robohash',
        'blank',
    ]
    RATINGS = [
        'g',
        'pg',
        'r',
        'x',
    ]
    PROFILE_FORMATS = ['json', 'xml', 'php', 'vcf', 'qr']

    def __init__(self, email):
        self.email = sanitize_email(email)
        self.email_hash = md5_hash(self.email)

    def get_image(self, size=DEFAULT_IMAGE_SIZE, default="", force_default=False, rating="", filetype_extension=False, use_ssl=False):
        """
        Returns an URL to the user profile image.

        >>> g = Gravatar('myemailaddress@example.com')
        >>> g.get_image()
        'http://www.gravatar.com/avatar/0bc83cb571cd1c50ba6f3e8a78ef1346'

        With *size* you can request a specific image size, by default, images are presented at 80px by 80px.
        You may request image anywhere from 1px up to 2048px.

        The *default* parameter is used to supply a default image when an email address has no match Gravatar image.
        *default* can be an URL or one of the built in options *404*, *mm*, *mp*, *identicon*, *monsterid*, *wavatar*, *robohash*, *retro* or *blank*.  

        *force_default* force the default image to always load.

        *rating* can be used to request images by audience type. Possible values are *g*, *pg*, *r* or *x*.
        By default, only *g* rated images are displayed.

        *filetype_extension* add an optional `.jpg` extension.

        *use_ssl* can be used to request images via SSL.

        See more details on `Gravatar Image Requests <http://en.gravatar.com/site/implement/images/>`_.

        """
        base_url = '{protocol}://{domain}/avatar/' \
            '{hash}{extension}{params}'

        params_dict = {
            'size': size,
            'default': default,
            'forcedefault': force_default,
            'rating': rating,
        }

        if params_dict['size'] == self.DEFAULT_IMAGE_SIZE:
            del params_dict['size']
        else:
            if not (0 < params_dict['size'] < 2048):
                raise ValueError('Invalid image size.')
        if params_dict['default'] == '':
            del params_dict['default']
        else:
            if not params_dict['default'] in self.DEFAULT_IMAGE:
                if not default_url_is_valid(params_dict['default']):
                    raise ValueError('Your URL for the default image is not valid.')
        if params_dict['forcedefault']:
            params_dict['forcedefault'] = 'y'
        else:
            del params_dict['forcedefault']
        if params_dict['rating'] == '':
            del params_dict['rating']
        else:
            if not params_dict['rating'] in self.RATINGS:
                raise ValueError('Invalid rating value.')

        params = urlencode(params_dict)

        protocol = 'http'
        domain = 'www.gravatar.com'
        if use_ssl:
            protocol = 'https'
            domain = 'secure.gravatar.com'

        extension = '.jpg' if filetype_extension else ''
        params = '?%s' % params if params else ''
        data = {
            'protocol': protocol,
            'domain': domain,
            'hash': self.email_hash,
            'extension': extension,
            'params': params,
        }
        return base_url.format(**data)

    def get_profile(self, data_format=''):
        """
        Returns an URL to the profile information associated with the Gravatar account.

        >>> g = Gravatar('myemailaddress@example.com')
        >>> g.get_profile()
        'http://www.gravatar.com/0bc83cb571cd1c50ba6f3e8a78ef1346'

        See more details on `Gravatar Profile Requests <http://en.gravatar.com/site/implement/profiles/>`_.

        """
        base_url = 'http://www.gravatar.com/{hash}{data_format}'

        if data_format and data_format in self.PROFILE_FORMATS:
            data_format = '.%s' % data_format

        data = {
            'hash': self.email_hash,
            'data_format': data_format,
        }
        return base_url.format(**data)

class GravatarXMLRPC(object):
    """
    This class encapsulates all the authenticated methods from the XML-RPC API.

    API details: http://en.gravatar.com/site/implement/xmlrpc
    """
    API_URI = 'https://secure.gravatar.com/xmlrpc?user={0}'

    def __init__(self, email, apikey='', password=''):
        self.apikey = apikey
        self.password = password
        self.email = sanitize_email(email)
        self.email_hash = md5_hash(self.email)
        self._server = ServerProxy(
            self.API_URI.format(self.email_hash))

    def exists(self, hashes):
        """Checks whether a hash has a gravatar."""
        response = self._call('exists', params={'hashes': hashes})
        results = {}
        for key, value in response.items():
            results[key] = True if value else False
        return results

    def addresses(self):
        """Gets a list of addresses for this account."""
        return self._call('addresses')

    def userimages(self):
        """Returns a dict of userimages for this account."""
        return self._call('userimages')

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
        except Fault as error:
            error_msg = "Server error: {1} (error code: {0})"
            print(error_msg.format(error.faultCode, error.faultString))


def sanitize_email(email):
    """
    Returns an e-mail address in lower-case and strip leading and trailing
    whitespaces.

    >>> sanitize_email(' MyEmailAddress@example.com ')
    'myemailaddress@example.com'

    """
    return email.lower().strip()


def md5_hash(string):
    """
    Returns a md5 hash from a string.

    >>> md5_hash('myemailaddress@example.com')
    '0bc83cb571cd1c50ba6f3e8a78ef1346'

    """
    return md5(string.encode('utf-8')).hexdigest()


def default_url_is_valid(url):
    """
    Gravatar conditions for valid default URLs.

    >>> default_url_is_valid('http://example.com/images/avatar.jpg')
    True

    """
    result = urlparse(url)

    if result.scheme == 'http' or result.scheme == 'https':
        path = result.path.lower()
        if (path.endswith('.jpg') or path.endswith('.jpeg')
            or path.endswith('.gif') or path.endswith('.png')):
            if not result.query:
                return True
    return False
