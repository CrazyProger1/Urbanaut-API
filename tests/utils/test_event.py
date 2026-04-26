import pytest

from src.utils.events import Event, EventChannel


def test_subscribe():
    ev = Event(name="test")

    ev.subscribe(print)

    assert print in ev.subscribers


def test_subscribe_not_callable():
    ev = Event(name="test")

    with pytest.raises(TypeError):
        ev.subscribe("")


def test_unsubscribe():
    ev = Event(name="test")

    ev.subscribe(print)
    ev.unsubscribe(print)

    assert print not in ev.subscribers


def test_is_subscriber():
    ev = Event(name="test")

    ev.subscribe(print)

    assert ev.is_subscriber(print)

    ev.unsubscribe(print)

    assert not ev.is_subscriber(print)


def test_publish():
    ev = Event(name="test")

    called = False

    def subs():
        nonlocal called

        called = True

    ev.subscribe(subs)

    ev.publish()

    assert called


def test_channel_prop():
    class Channel(EventChannel):
        ev = Event()

    assert Channel.ev.channel is Channel


def test_without_name():
    ev = Event()

    with pytest.raises(ValueError):
        print(ev)
