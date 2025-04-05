import logging

from src.apps.notifier.services.db import get_event_or_none, mark_event_completed
from src.apps.notifier.tasks.notifications import send_event_notifications
from src.apps.notifier.tasks.newsletters import send_event_newsletters

from src.config.celery import celery

logger = logging.getLogger(__name__)


@celery.task
def trigger_event(event_id: int):
    logger.info("Triggering event №%s...", event_id)
    event = get_event_or_none(pk=event_id)

    if not event:
        logger.warning("Event %s not found. Skipping...", event_id)
        return

    if not event.is_active:
        logger.warning(f"Event %s is not active. Skipping...", event_id)
        return

    send_event_notifications.delay(event_id)
    send_event_newsletters.delay(event_id)

    mark_event_completed(event=event)
    logger.info(f"Event №%s completed successfully.", event_id)
