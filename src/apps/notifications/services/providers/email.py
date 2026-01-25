import logging

from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.mail import send_mail

from src.apps.notifications.enums import NotificationProvider, NotificationAudience
from src.apps.notifications.models import Notification
from src.apps.notifications.services.providers import BaseProvider

User = get_user_model()

logger = logging.getLogger(__name__)


class EmailProvider(BaseProvider):
    PROVIDER = NotificationProvider.EMAIL

    def get_compatible_recipients(self, notification: Notification):
        if notification.audience == NotificationAudience.SYSTEM:
            return User.objects.filter(email__isnull=False)
        return notification.recipients.filter(email__isnull=False)

    def show(self, notification: Notification) -> None:
        emails = list(self.get_compatible_recipients(notification).values_list("email", flat=True))

        try:
            send_mail(
                subject=notification.title,
                message=notification.content,
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=emails,
                fail_silently=False,
            )
            logger.info("Email %s sent successfully", notification.title)
        except Exception as e:
            logger.error("Failed to send email: %s", str(e), exc_info=e)
