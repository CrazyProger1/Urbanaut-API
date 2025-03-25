from django.contrib.auth import get_user_model
from django.db import models
from django.db.models import QuerySet, Subquery, Q, OuterRef, Exists

from src.apps.notifications.models import Notification, NotificationStatus
from src.utils.db import filter_objects, get_all_objects
from src.apps.notifications.services.statuses import filter_notification_status

User = get_user_model()


def get_all_notifications() -> models.QuerySet[Notification]:
    return get_all_objects(Notification)


def get_user_notifications(user: User) -> models.QuerySet[Notification]:
    return (
        filter_objects(
            source=Notification,
            recipients=user,
            is_shown=True,
        )
        .order_by("-show_at")
    )


def annotate_is_read_notifications(notifications: QuerySet[Notification], user: User) -> models.QuerySet[Notification]:
    statuses = NotificationStatus.objects.filter(
        notification_id=OuterRef("id"),
        user=user,
    ).values("is_read")[:1]

    return notifications.annotate(
        is_read=Subquery(statuses),
    )


def mark_read(
        notifications: QuerySet[Notification],
        user: User,
) -> None:
    queryset = filter_notification_status(
        notification__in=notifications,
        user=user,
        is_read=False,
    )
    queryset.update(is_read=True)
