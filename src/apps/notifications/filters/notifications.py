from django_filters import rest_framework as filters

from src.apps.notifications.models import Notification
from src.apps.notifications.services.db import (
    get_enabled_notification_providers,
    filter_notifications_by_recipient_read,
)


class NotificationFilter(filters.FilterSet):
    providers = filters.ModelMultipleChoiceFilter(
        queryset=get_enabled_notification_providers(),
        field_name="providers__physical_provider",
        to_field_name="physical_provider",
    )
    is_read = filters.BooleanFilter(method="filter_by_is_read")

    class Meta:
        model = Notification
        fields = ("providers",)

    def filter_by_is_read(self, queryset, name, value):
        return filter_notifications_by_recipient_read(
            source=queryset,
            recipient=self.request.user,
            is_read=value,
        )
