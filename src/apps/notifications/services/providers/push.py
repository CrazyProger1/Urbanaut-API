import channels.layers
from asgiref.sync import async_to_sync
from django.conf import settings
from django.contrib.auth import get_user_model
from onesignal_sdk.client import AsyncClient

from src.apps.notifications.enums import NotificationAudience, NotificationProvider
from src.apps.notifications.models import Notification
from src.apps.notifications.serializers import NotificationSendSerializer
from src.apps.notifications.services.providers.types import BaseProvider

User = get_user_model()


class PushProvider(BaseProvider):
    PROVIDER = NotificationProvider.PUSH

    def get_audience(self, notification: Notification):
        if notification.audience == NotificationAudience.SYSTEM:
            return User.objects.filter(settings__is_notifications_enabled=True)
        return notification.recipients.filter(settings__is_notifications_enabled=True)

    def show(self, notification: Notification) -> None:
        client = AsyncClient(
            app_id=settings.ONESIGNAL_APP_ID,
            rest_api_key=settings.ONESIGNAL_API_KEY,
        )

        audience = self.get_audience(notification=notification)

        notification_body = {
            "contents": {
                "en": notification.subtitle,
            }
        }

        if notification.audience == NotificationAudience.SYSTEM:
            notification_body["included_segments"] = ["Active Subscriptions"]
        else:
            notification_body["include_external_user_ids"] = list(map(str, audience.values_list("id", flat=True)))

        async_to_sync(client.send_notification)(notification_body)
