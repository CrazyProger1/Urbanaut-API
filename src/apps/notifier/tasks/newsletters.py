import asyncio
import logging

from src.apps.notifier.services.db import (
    get_event_or_none,
    get_newsletter_target_users,
    get_newsletter_or_none,
)
from src.apps.notifier.services.newsletters import asend_newsletter
from src.config.celery import celery

logger = logging.getLogger(__name__)


@celery.task
def send_event_newsletter(event_id: int, newsletter_id: int):
    logger.info("Sending newsletter №%s for event №%s...", newsletter_id, event_id)

    event = get_event_or_none(pk=event_id)
    newsletter = get_newsletter_or_none(pk=newsletter_id)

    if not event:
        logger.warning("Event %s not found. Skipping...", event_id)
        return

    target_users = get_newsletter_target_users(event=event)
    loop = asyncio.get_event_loop()
    loop.run_until_complete(asend_newsletter(
        message=newsletter.message,
        user_ids=set(target_users.values_list("id", flat=True)),
    ))


@celery.task
def send_event_newsletters(event_id: int):
    logger.info("Sending newsletters for event №%s...", event_id)

    event = get_event_or_none(pk=event_id)

    if not event:
        logger.warning("Event %s not found. Skipping...", event_id)
        return

    newsletters = event.newsletters.all()

    for newsletter in newsletters:
        send_event_newsletter.delay(
            newsletter_id=newsletter.id,
            event_id=event_id,
        )

    logger.info("Newsletters sent for event №%s...", event_id)
