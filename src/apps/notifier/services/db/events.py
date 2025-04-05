from src.apps.notifier.models import Event
from src.utils.db import get_object_or_none


def get_event_or_none(*args, **kwargs) -> Event | None:
    return get_object_or_none(source=Event, *args, **kwargs)


def mark_event_completed(event: Event) -> None:
    event.is_active = False
    event.save(update_fields=["is_active"])
