from rest_framework import serializers

from src.apps.abandoned.models import AbandonedObject
from src.apps.abandoned.serializers.areas import AreaRetrieveSerializer


class ObjectListSerializer(serializers.ModelSerializer):
    class Meta:
        model = AbandonedObject
        fields = "__all__"


class ObjectRetrieveSerializer(serializers.ModelSerializer):
    area = AreaRetrieveSerializer(read_only=True)

    class Meta:
        model = AbandonedObject
        fields = "__all__"
