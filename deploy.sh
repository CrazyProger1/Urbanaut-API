#!/bin/bash

set -e

cd /home/admin/urbanaut/backend/ || exit

git checkout -- deploy.sh

git pull

mkdir -p logs

docker compose up --build --detach