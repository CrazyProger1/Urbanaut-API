import logging

from celery import shared_task

from src.apps.notifications.services.db import get_notification_or_none, mark_shown
from src.apps.notifications.services.websockets import (
    show_notification_via_websocket as show_notification_via_websocket,
)

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

    try:
        show_notification_via_websocket(notification)
        mark_shown(notification)
    except Exception as e:
        logger.exception("Failed to show notification #%s: %s", pk, e, exc_info=e)
        return

    logger.info("Notification #%s shown", pk)
