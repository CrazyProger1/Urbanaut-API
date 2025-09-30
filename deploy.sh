#!/bin/bash

set -e

cd /home/admin/urbanaut/backend/ || exit

git checkout -- deploy.sh

git pull

poetry install --no-root

poetry run python manage.py migrate
poetry run python manage.py collectstatic --noinput

supervisorctl restart backend

mkdir -p logs