from src.apps.notifications.models import NotificationProvider


def get_enabled_notification_providers():
    return NotificationProvider.objects.filter(is_enabled=True)
