from django.contrib.auth import get_user_model
from django.db import models
from django.db.models import QuerySet, Subquery, OuterRef

from src.apps.notifier.models import Notification, NotificationStatus
from src.utils.db import filter_objects, get_all_objects, get_object_or_error

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
        .order_by("-shown_at")
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


def get_notification_status_or_error(**data) -> NotificationStatus:
    return get_object_or_error(
        NotificationStatus,
        **data,
    )


def filter_notification_status(**data):
    return filter_objects(NotificationStatus, **data)
