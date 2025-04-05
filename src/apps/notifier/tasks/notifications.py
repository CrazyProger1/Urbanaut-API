import logging

from django.utils import timezone

from src.apps.notifier.services.db import get_event_or_none, get_notification_target_users
from src.config.celery import celery

logger = logging.getLogger(__name__)


@celery.task
def send_event_notifications(event_id: int):
    logger.info("Sending notifications for event №%s...", event_id)

    event = get_event_or_none(pk=event_id)

    if not event:
        logger.warning("Event %s not found. Skipping...", event_id)
        return

    target_users = get_notification_target_users(event=event)
    notifications = event.notifications

    notifications.update(
        shown_at=timezone.now(),
        is_shown=True,
        recipients=target_users,
    )

    logger.info("Notifications sent for event №%s...", event_id)
