from rest_framework import serializers

from src.apps.abandoned.models import AbandonedObject
from src.apps.abandoned.serializers.areas import AbandonedAreaRetrieveSerializer
from src.apps.accounts.serializers import UserRetrieveSerializer


class AbandonedObjectListSerializer(serializers.ModelSerializer):
    class Meta:
        model = AbandonedObject
        fields = "__all__"


class AbandonedObjectRetrieveSerializer(serializers.ModelSerializer):
    area = AbandonedAreaRetrieveSerializer(read_only=True)
    creator = UserRetrieveSerializer(read_only=True)

    class Meta:
        model = AbandonedObject
        fields = "__all__"


class AbandonedObjectCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = AbandonedObject
        exclude = (
            "created_at",
            "updated_at",
            "is_hidden",
            "creator",
        )
