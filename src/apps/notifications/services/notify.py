import logging
from datetime import datetime
from typing import Iterable

from django.db import transaction

from django.utils import timezone

from src.apps.accounts.models import User
from src.apps.notifications.enums import (
    NotificationProvider as PhysicalNotificationProvider,
    NotificationAudience,
    NotificationType,
    NotificationProvider,
)
from src.apps.notifications.models import Notification, NotificationRecipient, NotificationProvider
from src.utils.django.beat import plan_execution
from src.apps.notifications.tasks import show_notification

logger = logging.getLogger(__name__)


def _localized_field(basename: str, translations: dict) -> dict:
    result = {}
    for lang, trans in translations.items():
        if not lang:
            result[basename] = trans
        else:
            result[f"{basename}_{lang}"] = trans
    return result


def _resolve_providers(providers: Iterable[PhysicalNotificationProvider]) -> list[NotificationProvider]:
    if not providers:
        return []

    resolved = []
    for provider in providers:
        provider_obj = NotificationProvider.objects.filter(physical_provider=provider).first()
        if provider_obj:
            resolved.append(provider_obj)

    return resolved


@transaction.atomic
def notify(
        title: dict,
        subtitle: dict = None,
        content: dict = None,
        now: bool = False,
        trigger_at: datetime = None,
        providers: Iterable[PhysicalNotificationProvider] = None,
        audience: NotificationAudience = None,
        users: Iterable[User] = None,
        tp: NotificationType = None,
        initiator: User = None,
):
    if not now and not trigger_at:
        raise RuntimeError("Earthier now or trigger_at must be specified to notify user")

    kwargs = {}

    kwargs.update(_localized_field("title", title))

    if subtitle:
        kwargs.update(_localized_field("subtitle", subtitle))

    if content:
        kwargs.update(_localized_field("content", content))

    logger.debug("Creating notification: type=%s, audience=%s, now=%s, trigger_at=%s", tp, audience, now, trigger_at)

    notification = Notification.objects.create(
        type=tp,
        audience=audience,
        triggered_at=trigger_at,
        created_by=initiator,
        **kwargs,
    )
    notification.providers.set(_resolve_providers(providers=providers))
    logger.debug("Notification %s created", notification.pk)

    if users:
        users = list(users)
        NotificationRecipient.objects.bulk_create(
            [NotificationRecipient(user=user, notification=notification) for user in users])
        logger.debug("Created %s recipients for notification %s", len(users), notification.pk)

    if now:
        logger.debug("Dispatching notification %s immediately", notification.pk)
        show_notification.apply_async((notification.pk,), countdown=5)
    else:
        logger.debug("Scheduling notification %s at %s", notification.pk, notification.triggered_at)
        plan_execution(
            task_id=f"show_notification_{notification.pk}",
            task="src.apps.notifications.tasks.notifications.show_notification",
            execute_at=notification.triggered_at or timezone.now(),
            args=(notification.pk,),
        )
