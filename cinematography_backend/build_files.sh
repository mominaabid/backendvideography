#!/bin/bash
pip install -r requirements.txt
python3 manage.py collectstatic --noinput
python3 manage.py migrate
gunicorn cinematography_backend.wsgi
