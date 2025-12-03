from rest_framework import serializers

from src.apps.feedbacks.models import Feedback


class FeedbackCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = ("content", "id")
        read_only_fields = ("id",)
