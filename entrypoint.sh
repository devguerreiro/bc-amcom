#!/bin/sh

python manage.py migrate
python manage.py createsuperuser --noinput --email ${DJANGO_SUPERUSER_USERNAME}@${DJANGO_SUPERUSER_USERNAME}.com
python manage.py runserver 0.0.0.0:${PORT}
