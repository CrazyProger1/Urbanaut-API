from rest_framework import serializers

from src.apps.notifications.models import Notification


class NotificationListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        exclude = ("recipients",)


class NotificationRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        exclude = ("recipients",)
