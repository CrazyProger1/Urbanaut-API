from src.apps.notifications.models import NotificationStatus
from src.utils.db import filter_objects, get_object_or_error


def get_notification_status_or_error(**data) -> NotificationStatus:
    return get_object_or_error(
        NotificationStatus,
        **data,
    )


def filter_notification_status(**data):
    return filter_objects(NotificationStatus, **data)
