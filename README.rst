================
Gravatar XML-RPC
================

A library that provides a Python 3 interface to the Gravatar XML-RPC API.
API Details: http://en.gravatar.com/site/implement/xmlrpc

Author
------

Pablo Seminario <pabluk@gmail.com>

Usage
-----

Getting user profile image
::

    from gravatar import Gravatar
    g = Gravatar('myemailaddress@example.com')
    g.get_image()
    'http://www.gravatar.com/avatar/0bc83cb571cd1c50ba6f3e8a78ef1346.jpg?size=80'

If you have an account at Wordpress.com you can use your API Key
::

    from gravatar import GravatarXMLRPC
    g = GravatarXMLRPC('user@domain', apikey='1234')
    g.test() # test the API

Or you can use your Gravatar.com password
::

    from gravatar import GravatarXMLRPC
    g = GravatarXMLRPC('user@domain', password='1234')
    g.test() # test the API

License
-------

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
