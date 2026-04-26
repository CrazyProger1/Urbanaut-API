import pytest

from src.utils.events import Event, EventChannel


def test_events():
    class Channel(EventChannel):
        e1 = Event()
        e2 = Event()

    assert Channel.e1 in Channel.events
    assert Channel.e2 in Channel.events


def test_iter():
    class Channel(EventChannel):
        e1 = Event()
        e2 = Event()

    assert Channel.e1 in tuple(Channel)
    assert len(tuple(Channel)) == 2


def test_contains():
    class Channel(EventChannel):
        e1 = Event()
        e2 = Event()

    assert Channel.e1.name in Channel


def test_getitem():
    class Channel(EventChannel):
        e1 = Event()
        e2 = Event()

    assert Channel.e1 is Channel["e1"]

    with pytest.raises(KeyError):
        e4 = Channel["e4"]
