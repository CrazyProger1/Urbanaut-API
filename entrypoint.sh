#!/bin/bash
set -e

echo "Running migrations..."
uv run python manage.py migrate

echo "Creating superuser..."
uv run python manage.py createsuperuser --no-input || true

echo "Starting uvicorn server..."
uv run uvicorn src.config.web.asgi:application --host 0.0.0.0 --port 8001 --log-level debug --workers 4 --reload