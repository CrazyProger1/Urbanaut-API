from rest_framework import serializers

from src.apps.notifier.models import Notification


class NotificationListSerializer(serializers.ModelSerializer):
    is_read = serializers.SerializerMethodField()

    class Meta:
        model = Notification
        fields = (
            "title",
            "shown_at",
            "message",
            "type",
            "icon",
            "is_read",
        )

    def get_is_read(self, obj: Notification) -> bool:
        return getattr(obj, "is_read", False)


class NotificationRetrieveSerializer(serializers.ModelSerializer):
    is_read = serializers.SerializerMethodField()

    class Meta:
        model = Notification
        fields = (
            "title",
            "shown_at",
            "is_shown",
            "message",
            "type",
            "icon",
            "is_read",
        )

    def get_is_read(self, obj: Notification) -> bool:
        return getattr(obj, "is_read", False)
