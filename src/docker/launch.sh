#!/usr/bin/env bash

while ! nc -z $POSTGRES_HOST $PGPORT; do
      sleep 0.1
done 

python manage.py migrate

gunicorn --bind 0.0.0.0:8000 src.wsgi:application --workers 3
