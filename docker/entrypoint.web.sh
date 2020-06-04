#!/bin/sh

python ./manage.py collectstatic
python ./manage.py migrate

gunicorn emarket.wsgi -c gunicorn/gunicorn.conf.py
