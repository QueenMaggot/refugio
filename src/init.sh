#!/bin/bash
python manage.py migrate
python manage.py collectstatic --noinput
python manage.py loaddata backup_utf8.json