#!/bin/sh
python manage.py makemigrations
python manage.py migrate
# python manage.py runserver 0.0.0.0:8000
gunicorn Eshop.wsgi:application --bind 0.0.0.0:8000
