from src.utils.events import EventChannel, Event


class PlaceEventChannel(EventChannel):
    place_created = Event()
    place_removed_by_moderator = Event()
