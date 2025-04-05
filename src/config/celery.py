import os

from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "src.config.settings")

from django.conf import settings

celery = Celery(settings.TITLE)

celery.config_from_object("django.conf:settings", namespace="CELERY")

celery.autodiscover_tasks(["src.apps.notifier.tasks"])
