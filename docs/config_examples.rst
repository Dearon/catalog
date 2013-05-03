
======================
Configuration examples
======================

These examples show how to get the development environment up using nginx_ and supervisor_.

-----
Nginx
-----

::

    server {
        listen      80;
        server_name www.domain.com;

        root        /srv/django/catalog/catalog;

        location /assets {
            alias/srv/django/catalog/catalog/assets/;
        }

        location / {
            proxy_pass_header Server;
            proxy_set_header Host $http_host;
            proxy_redirect off;
            proxy_set_header X-Real-IP $remote_addr;
            proxy_set_header X-Scheme $scheme;
            proxy_connect_timeout 10;
            proxy_pass http://localhost:8000/;
        }
    }

----------
Supervisor
----------

::

    [program:catalog]
    directory=/srv/django/catalog
    user=http
    command=/srv/django/catalog/catalog/manage.py run_gunicorn -b 127.0.0.1:8000 -w 3 --settings catalog.settings.local
    environment=
        PATH='/srv/django/catalog/bin',
        SECRET_KEY='secret_key',
        DATABASE_NAME='name',
        DATABASE_USER='user',
        DATABASE_PASSWORD='password'
    stdout_logfile=/var/log/supervisor/stdout.log
    stderr_logfile=/var/log/supervisor/stderr.log

.. _nginx: http://nginx.com
.. _supervisor: https://pypi.python.org/pypi/supervisor
