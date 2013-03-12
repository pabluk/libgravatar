===========
libgravatar
===========


.. image:: https://travis-ci.org/pabluk/libgravatar.png?branch=master
        :target: https://travis-ci.org/pabluk/libgravatar

A library that provides a Python 3 interface for the Gravatar API.
API details: https://en.gravatar.com/site/implement/

Installation
------------

Install via pip::

    $ pip install libgravatar


Usage
-----

See more details on https://libgravatar.readthedocs.org/

Gravatar API
~~~~~~~~~~~~

Gravatar API require no authentication to get images and profiles URLs.

Getting the user profile image::

    from libgravatar import Gravatar
    g = Gravatar('myemailaddress@example.com')
    g.get_image()
    'http://www.gravatar.com/avatar/0bc83cb571cd1c50ba6f3e8a78ef1346'

Getting the profile URL::

    from libgravatar import Gravatar
    g = Gravatar('myemailaddress@example.com')
    g.get_profile()
    'http://www.gravatar.com/0bc83cb571cd1c50ba6f3e8a78ef1346'


Gravatar XML-RPC API
~~~~~~~~~~~~~~~~~~~~

The XML-RPC API require authentication.

You can use your Gravatar.com password::

    from libgravatar import GravatarXMLRPC
    g = GravatarXMLRPC('user@domain', password='1234')
    g.test() # test the API


or if you have an account at Wordpress.com you can use your API Key::

    from libgravatar import GravatarXMLRPC
    g = GravatarXMLRPC('user@domain', apikey='1234')
    g.test() # test the API

