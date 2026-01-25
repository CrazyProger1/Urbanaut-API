from django.db.models import Q
from django.utils import timezone

from src.apps.notifications.enums import NotificationAudience
from src.apps.notifications.models import Notification, NotificationRecipient
from src.utils.django.db import Source, get_queryset


def get_all_notifications():
    return Notification.objects.all().order_by("-triggered_at")


def get_user_notifications(user):
    return Notification.objects.filter(
        Q(recipients=user) | Q(audience=NotificationAudience.SYSTEM)
    ).order_by("-triggered_at")


def filter_notifications_by_recipient_read(
    source: Source[Notification],
    recipient,
    is_read: bool,
):
    queryset = get_queryset(source=source)
    return (
        queryset.filter(
            Q(
                recipients__in=NotificationRecipient.objects.filter(
                    is_read=is_read,
                    user=recipient,
                ).values("user")
            )
            | (Q(audience=NotificationAudience.SYSTEM) & ~Q(recipients__in=[recipient]))
        )
        .distinct()
        .order_by("-triggered_at")
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
