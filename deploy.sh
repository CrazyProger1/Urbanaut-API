#!/bin/bash

set -e

cd /home/admin/urbanaut/backend/ || exit

git checkout -- deploy.sh

git pull

/home/admin/.local/bin/uv run python manage.py migrate
/home/admin/.local/bin/uv run python manage.py collectstatic --noinput

supervisorctl restart backend

mkdir -p logs