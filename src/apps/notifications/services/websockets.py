import channels.layers
from asgiref.sync import async_to_sync

from src.apps.notifications.models import Notification
from src.apps.notifications.serializers import NotificationSendSerializer


def show_notification_via_websocket(notification: Notification):
    channel_layer = channels.layers.get_channel_layer()
    serializer = NotificationSendSerializer(instance=notification)
    async_to_sync(channel_layer.group_send)("system", {"notification": serializer.data, "type": "send_notification"})
