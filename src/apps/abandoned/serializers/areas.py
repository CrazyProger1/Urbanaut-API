from rest_framework import serializers

from src.apps.abandoned.models import AbandonedArea


class AreaListSerializer(serializers.ModelSerializer):
    class Meta:
        model = AbandonedArea
        fields = "__all__"


class AreaRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = AbandonedArea
        fields = "__all__"
