#!/bin/bash

set -e

cd /home/admin/urbanaut/backend/ || exit

git checkout -- deploy.sh

git pull

uv run python manage.py migrate
uv run python manage.py collectstatic --noinput

supervisorctl restart backend

mkdir -p logs