import channels.layers
from asgiref.sync import async_to_sync
from django.conf import settings

from src.apps.notifications.enums import NotificationAudience
from src.apps.notifications.models import Notification
from src.apps.notifications.serializers import NotificationSendSerializer


def show_notification_via_websocket(notification: Notification):
    channel_layer = channels.layers.get_channel_layer()
    serializer = NotificationSendSerializer(instance=notification)
    data = {
        "data": serializer.data,
        "type": "send_event",
        "event": settings.WEBSOCKET_EVENT_NOTIFICATION,
    }

    if notification.audience == NotificationAudience.SYSTEM:
        async_to_sync(channel_layer.group_send)(
            settings.WEBSOCKET_SYSTEM_GROUP,
            data,
        )
    elif notification.audience == NotificationAudience.GROUP:
        for recipient in notification.recipients.all():
            async_to_sync(channel_layer.group_send)(
                settings.WEBSOCKET_USER_GROUP.format(id=recipient.id),
                data,
            )
    else:
        recipient = notification.recipients.first()
        async_to_sync(channel_layer.group_send)(
            settings.WEBSOCKET_USER_GROUP.format(id=recipient.id),
            data,
        )
