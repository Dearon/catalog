
Installation
============

------------
Dependencies
------------

- A HTTP server (e.g. nginx_)

- A database (e.g. PostgreSQL_)

- `Python 2`_ and virtualenv_

------------
Installation
------------

- Create a user and database for the site to use

- Create a virtualenviroment, e.g.::

    $ virtualenv2 --no-site-packages catalog


- Clone the git respository into the virtualenv directory::

    $ git clone git@github.com:Dearon/catalog.git


- Install the required libraries::

    $ cd catalog
    $ source bin/active
    $ pip install -r requirments/local.txt


- Set the environment variables up. I usually create a export.sh so that I can do source export.sh, the content of this file is::

    export SECRET_KEY='secret key'
    export DATABASE_NAME='name'
    export DATABASE_USER='user'
    export DATABASE_PASSWORD='password'


- Sync the datase::

    $ cd catalog
    $ ./manage.py syncdb --settings catalog.settings.local


- Configure your webserver and it should work.

-----
Notes
-----

See :doc:`config_examples` for configuration examples and the :doc:`faq` for general information.


.. _nginx: http://nginx.com/
.. _PostgreSQL: http://www.postgresql.org/
.. _Python 2: http://python.org/
.. _virtualenv: https://pypi.python.org/pypi/virtualenv
