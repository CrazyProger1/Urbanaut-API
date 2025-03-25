#!/bin/bash

cd /home/urbanaut/backend/ || exit
git pull

source /home/urbanaut/backend/.venv/bin/activate

python manage.py migrate

python manage.py collectstatic --noinput

sudo supervisorctl restart backend
