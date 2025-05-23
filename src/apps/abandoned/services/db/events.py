from src.apps.abandoned.models import Event
from src.utils.db import get_all_objects


def get_all_events():
    return get_all_objects(source=Event)


def get_available_events(user=None):
    return Event.objects.visible(user=user)


def count_user_events(user) -> int:
    return user.my_events.count()
