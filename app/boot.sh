#!/bin/bash

# ensure db is up-to-date
flask db upgrade

# run gunicorn web server
exec gunicorn -b :5000 wsgi:app