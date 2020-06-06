#!/bin/sh

python ./manage.py collectstatic --noinput
python ./manage.py migrate

gunicorn emarket.wsgi -c config/gunicorn/gunicorn.conf.py
