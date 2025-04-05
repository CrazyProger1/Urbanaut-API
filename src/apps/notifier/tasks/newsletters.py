import logging

from src.apps.notifier.services.db import get_event_or_none
from src.config.celery import celery

logger = logging.getLogger(__name__)


@celery.task
def send_event_newsletters(event_id: int):
    event = get_event_or_none(pk=event_id)
    if not event:
        logger.warning("Event %s not found. Skipping...", event_id)
        return
