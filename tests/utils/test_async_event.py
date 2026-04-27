import pytest

from src.utils.events import AsyncEvent, EventChannel


@pytest.mark.asyncio
async def test_publish_async():
    ev = AsyncEvent(name="test")

    called = False

    async def subs():
        nonlocal called

        called = True

    ev.subscribe(subs)

    await ev.publish_async()

    assert called


@pytest.mark.parametrize(
    "options, result", (({"nonblocking": True}, False), ({"nonblocking": False}, True))
)
@pytest.mark.asyncio
async def test_nonblocking(options, result):
    ev = AsyncEvent(name="test", **options)

    called = False

    def subs():
        nonlocal called

        called = True

    ev.subscribe(subs)

    await ev.publish_async()

    assert called is result
