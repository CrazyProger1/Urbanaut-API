#!/bin/bash

cd /home/urbanaut/backend/ || exit
git pull

poetry install --no-root

poetry run python manage.py migrate
poetry run python manage.py collectstatic --noinput

sudo supervisorctl restart backend
