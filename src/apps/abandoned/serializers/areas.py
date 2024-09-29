from rest_framework import serializers

from src.apps.abandoned.models import AbandonedArea


class AbandonedAreaListSerializer(serializers.ModelSerializer):
    class Meta:
        model = AbandonedArea
        fields = "__all__"


class AbandonedAreaRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = AbandonedArea
        fields = "__all__"
