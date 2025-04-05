import logging

from src.apps.notifier.services.db import get_event_or_none, mark_event_completed
from src.config.celery import celery

logger = logging.getLogger(__name__)


@celery.task
def trigger_event(event_id: int):
    event = get_event_or_none(pk=event_id)

    if not event.is_active:
        logger.warning(f"Event {event_id} is not active. Skipping...")
        return

    mark_event_completed(event=event)
    logger.info(f"Event {event_id} completed successfully.")
