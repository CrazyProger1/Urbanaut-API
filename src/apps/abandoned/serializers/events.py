from rest_framework import serializers

from src.apps.abandoned.models import Event


class EventListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = (
            "id",
            "name",
            "short_description",
            "start_at",
            "end_at",
            "status",
        )


class EventRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = (
            "id",
            "name",
            "short_description",
            "start_at",
            "end_at",
            "status",
        )
