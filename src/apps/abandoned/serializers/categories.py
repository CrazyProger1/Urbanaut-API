from rest_framework import serializers

from src.apps.abandoned.models import AbandonedObjectCategory


class AbandonedObjectCategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = AbandonedObjectCategory
        fields = (
            "id",
            "name",
        )


class AbandonedObjectCategoryRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = AbandonedObjectCategory
        fields = (
            "id",
            "name",
            "description",
        )
