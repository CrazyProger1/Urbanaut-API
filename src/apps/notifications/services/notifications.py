from django.contrib.auth import get_user_model
from django.db import models
from django.db.models import QuerySet

from src.apps.notifications.models import Notification
from src.utils.db import filter_objects, get_all_objects
from src.apps.notifications.services.statuses import filter_notification_status

User = get_user_model()


def get_all_notifications() -> models.QuerySet[Notification]:
    return get_all_objects(Notification)


def get_user_notifications(user: User) -> models.QuerySet[Notification]:
    return filter_objects(
        Notification,
        recipients=user,
        is_shown=True,
    ).order_by("-show_at")


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
