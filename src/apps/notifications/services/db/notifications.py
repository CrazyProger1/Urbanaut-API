from django.utils import timezone

from src.apps.notifications.models import Notification, NotificationRecipient
from src.utils.django.db import Source, get_queryset


def get_all_notifications():
    return Notification.objects.all()


def get_user_notifications(user):
    return Notification.objects.filter(recipients=user)


def filter_notifications_by_recipient_read(
        source: Source[Notification], recipient, is_read: bool
):
    queryset = get_queryset(source=source)
    return queryset.filter(
        recipients__in=NotificationRecipient.objects.filter(
            is_read=is_read,
            user=recipient,
        ).values("user"),
    )


def get_notification_or_none(**data) -> Notification | None:
    return Notification.objects.filter(**data).first()


def mark_shown(notification: Notification):
    notification.is_shown = True
    notification.triggered_at = timezone.now()
    notification.save(
        update_fields=(
            "is_shown",
            "triggered_at",
        )
    )
