#!/bin/bash

cd /home/urbanaut/backend/ || exit

git pull

poetry install --no-root

#poetry run python manage.py makemigrations
poetry run python manage.py migrate
poetry run python manage.py collectstatic --noinput

supervisorctl restart backend
