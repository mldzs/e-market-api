#!/bin/sh

celery -A emarket.celery worker --loglevel=info
