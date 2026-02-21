from rest_framework import serializers

from src.apps.feedbacks.models import Request


class RequestCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Request
        fields = (
            "context",
            "type",
            "path",
        )
