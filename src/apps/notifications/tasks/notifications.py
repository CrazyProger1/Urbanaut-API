import logging

from celery import shared_task

from src.apps.notifications.services.db import get_notification_or_none, mark_shown

from src.apps.notifications.enums import NotificationProvider as PhysicalNotificationProvider
from src.apps.notifications.services.providers import BaseProvider

logger = logging.getLogger(__name__)


@shared_task
def show_notification_via_provider(pk, provider: PhysicalNotificationProvider):
    notification = get_notification_or_none(pk=pk)

    if not notification:
        logger.error("No notification found with pk = %s", pk)
        return

    provider = BaseProvider.get_provider(provider=provider)

    try:
        provider.show(notification=notification)
        logger.info("Notification #%s shown via %s", pk, provider)
    except Exception as e:
        logger.exception("Failed to show notification #%s: %s", pk, e, exc_info=e)


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
        providers = set(notification.providers.values_list("physical_provider", flat=True))

        for provider in providers:
            show_notification_via_provider.delay(pk=pk, provider=provider)

        mark_shown(notification)
    except Exception as e:
        logger.exception("Failed to show notification #%s: %s", pk, e, exc_info=e)
        return

    logger.info("Notification #%s shown", pk)
