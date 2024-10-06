from rest_framework import serializers

from src.apps.notifications.models import Notification


class NotificationListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = (
            "title",
            "show_at",
            "is_shown",
            "message",
            "type",
            "icon",
        )


class NotificationRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = (
            "title",
            "show_at",
            "is_shown",
            "message",
            "type",
            "icon",
        )
