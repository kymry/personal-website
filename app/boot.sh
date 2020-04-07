#!/bin/bash

# run gunicorn web server
exec gunicorn -b 5000:5000 wsgi:app