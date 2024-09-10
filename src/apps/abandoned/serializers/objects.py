from rest_framework import serializers

from src.apps.abandoned.models import AbandonedObject
from src.apps.abandoned.serializers.areas import AbandonedAreaRetrieveSerializer
from src.apps.accounts.serializers import UserRetrieveSerializer
from src.apps.geo.serializers import LocationRetrieveSerializer, LocationCreateSerializer


class AbandonedObjectListSerializer(serializers.ModelSerializer):
    class Meta:
        model = AbandonedObject
        fields = "__all__"


class AbandonedObjectRetrieveSerializer(serializers.ModelSerializer):
    area = AbandonedAreaRetrieveSerializer(read_only=True)
    creator = UserRetrieveSerializer(read_only=True)
    location = LocationRetrieveSerializer(read_only=True)

    class Meta:
        model = AbandonedObject
        fields = "__all__"


class AbandonedObjectCreateSerializer(serializers.ModelSerializer):
    location = LocationCreateSerializer()

    class Meta:
        model = AbandonedObject
        exclude = (
            "created_at",
            "updated_at",
            "is_hidden",
            "creator",
        )
