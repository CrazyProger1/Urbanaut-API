from rest_framework import serializers

from src.apps.abandoned.models import Event
from src.apps.accounts.serializers import UserListSerializer, UserRetrieveSerializer


class EventListSerializer(serializers.ModelSerializer):
    created_by = UserListSerializer(read_only=True)

    class Meta:
        model = Event
        fields = (
            "id",
            "name",
            "short_description",
            "start_at",
            "end_at",
            "status",
            "created_by",
        )


class EventRetrieveSerializer(serializers.ModelSerializer):
    created_by = UserRetrieveSerializer(read_only=True)

    class Meta:
        model = Event
        fields = (
            "id",
            "name",
            "short_description",
            "start_at",
            "end_at",
            "status",
            "created_by",
        )
