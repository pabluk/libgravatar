===========
libgravatar
===========


.. image:: https://github.com/pabluk/libgravatar/actions/workflows/python-package.yml/badge.svg
        :target: https://github.com/pabluk/libgravatar/actions/workflows/python-package.yml

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

Gravatar API requires no authentication to get images and profiles URLs.

Getting the user profile image:

.. code-block:: python

    from libgravatar import Gravatar
    g = Gravatar('myemailaddress@example.com')
    g.get_image()
    'https://www.gravatar.com/avatar/0bc83cb571cd1c50ba6f3e8a78ef1346'

Getting the profile URL:

.. code-block:: python

    from libgravatar import Gravatar
    g = Gravatar('myemailaddress@example.com')
    g.get_profile()
    'https://www.gravatar.com/0bc83cb571cd1c50ba6f3e8a78ef1346'


Gravatar XML-RPC API
~~~~~~~~~~~~~~~~~~~~

The XML-RPC API requires authentication.

You can use your Gravatar.com's email and password:

.. code-block:: python

    from libgravatar import GravatarXMLRPC
    g = GravatarXMLRPC('name@example.com', password='1234')
    g.test() # test the API


or if you have an account at Wordpress.com you can use your email and
API key. You can find your API key at https://apikey.wordpress.com/
just be sure to pass to the function your email instead of your username:

.. code-block:: python

    from libgravatar import GravatarXMLRPC
    g = GravatarXMLRPC('name@example.com', apikey='1234')
    g.test() # test the API


Development
-----------

To contribute to this project or to test this library locally you'll need to install these dependencies:

.. code-block:: shell

    python3 -m venv venv # for example on a virtual environment
    source venv/bin/activate
    pip install nose black

and you can validate your changes running:

.. code-block:: shell

    nosetests --with-doctest --verbose
    black . --check --diff


Author and contributors
-----------------------

* Pablo Seminario (`@pabluk <https://github.com/pabluk>`_)
* Caleb FANGMEIER (`@cfangmeier <https://github.com/cfangmeier>`_)
* Rarm NAGALINGAM (`@snowjet <https://github.com/snowjet/>`_)
* Manan (`@mentix02 <https://github.com/mentix02/>`_)
* Gareth Simpson (`@xurble <https://github.com/xurble/>`_)
