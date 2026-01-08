# Deploying Without Docker

## Dependencies

Make sure you have the following dependencies installed:

- Python 3.12+
- Poetry
- PostgreSQL
- Redis

## Environment Variables

Create an .env file from [example](../.env.sample) and fill in the required values.

## Supervisorctl

backend.conf

```
[program:backend]
command=poetry run uvicorn src.config.asgi:application --host 0.0.0.0 --port 8000 --log-level debug --workers 4 --reload
directory=/home/urbanaut/backend/
autostart=true
autorestart=true
stderr_logfile=/home/urbanaut/backend/logs/err.log
stdout_logfile=/home/urbanaut/backend/logs/out.log
```

celery.conf

```
[program:celery]
command=poetry run celery -A src.config.celery worker --loglevel=INFO
directory=/home/urbanaut/backend/
autostart=true
autorestart=true
stderr_logfile=/home/urbanaut/backend/logs/celery.err.log
stdout_logfile=/home/urbanaut/backend/logs/celery.out.log
```

celery_beat.conf

```
[program:celery-beat]
command=poetry run celery -A src.config.celery beat --loglevel=INFO
directory=/home/urbanaut/backend/
autostart=true
autorestart=true
stderr_logfile=/home/urbanaut/backend/logs/celery-beat.err.log
stdout_logfile=/home/urbanaut/backend/logs/celery-beat.out.log
```

celery_flower.conf

```
[program:celery-flower]
command=poetry run celery -A src.config.celery flower --loglevel=INFO
directory=/home/urbanaut/backend/
autostart=true
autorestart=true
stderr_logfile=/home/urbanaut/backend/logs/celery-flower.err.log
stdout_logfile=/home/urbanaut/backend/logs/celery-flower.out.log
```
