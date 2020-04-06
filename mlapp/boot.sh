#!/bin/bash

# run gunicorn web server
exec gunicorn -b 5001:5001 wsgi:app