from django.contrib.auth import get_user_model
from django.db import models

from src.apps.notifier.models import Event
from src.utils.db import get_object_or_none

User = get_user_model()


def get_event_or_none(*args, **kwargs) -> Event | None:
    return get_object_or_none(source=Event, *args, **kwargs)


def mark_event_completed(event: Event) -> None:
    event.is_active = False
    event.save(update_fields=["is_active"])


def get_notification_target_users(event: Event) -> models.QuerySet[User]:
    users = User.objects.none()

    for category in event.categories.all():
        users |= category.recipients.all()

    return users
