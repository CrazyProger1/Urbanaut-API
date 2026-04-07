from rest_framework import serializers

from src.apps.accounts.serializers import UserListSerializer
from src.apps.expeditions.enums import ExpeditionState
from src.apps.expeditions.models import Expedition


class ExpeditionListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expedition
        fields = (
            "id",
            "name",
            "state",
            "started_at",
            "ended_at",
        )


class ExpeditionRetrieveSerializer(serializers.ModelSerializer):
    created_by = UserListSerializer(read_only=True)

    class Meta:
        model = Expedition
        fields = "__all__"


class ExpeditionCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expedition
        fields = (
            "name",
            "description",
            "started_at",
            "ended_at",
            "state",
        )
