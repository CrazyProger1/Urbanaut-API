import logging

from celery import shared_task

from src.apps.notifications.services.db import get_notification_or_none, mark_shown

logger = logging.getLogger(__name__)


@shared_task
def show_notification(pk):
    logger.info("Showing notification #%s", pk)

    notification = get_notification_or_none(pk=pk)

    if not notification:
        logger.error("No notification found with pk = %s", pk)
        return

    if notification.is_shown:
        logger.warning("Notification #%s is already shown", pk)
        return

    mark_shown(notification)

    logger.info("Notification #%s shown", pk)
