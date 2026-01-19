import channels.layers
from asgiref.sync import async_to_sync
from django.conf import settings

from src.apps.notifications.enums import NotificationAudience, NotificationProvider
from src.apps.notifications.models import Notification
from src.apps.notifications.serializers import NotificationSendSerializer
from src.apps.notifications.services.providers.types import BaseProvider


class WebsiteProvider(BaseProvider):
    PROVIDER = NotificationProvider.WEBSITE

    def get_compatible_recipients(self, notification: Notification):
        return notification.recipients.filter(is_online=True)

    def show(self, notification: Notification) -> None:
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
        else:
            for recipient in self.get_compatible_recipients(notification=notification):
                async_to_sync(channel_layer.group_send)(
                    settings.WEBSOCKET_USER_GROUP.format(id=recipient.id),
                    data,
                )
