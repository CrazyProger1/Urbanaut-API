import channels.layers
from asgiref.sync import async_to_sync

from src.apps.notifications.models import Notification


def show_notification_via_websocket():
    channel_layer = channels.layers.get_channel_layer()
    async_to_sync(channel_layer.send)("notifications", {"type": "status_check"})
