from src.utils.events import EventChannel, Event


class PlaceEventChannel(EventChannel):
    place_created = Event()
