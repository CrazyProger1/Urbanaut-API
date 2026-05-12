from rest_framework import serializers

from src.apps.accounts.models import Team
from src.apps.accounts.serializers import UserListSerializer


class TeamListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = (
            "id",
            "name",
        )


class TeamRetrieveSerializer(serializers.ModelSerializer):
    members = UserListSerializer(read_only=True, many=True)
    created_by = UserListSerializer(read_only=True, many=False)

    class Meta:
        model = Team
        fields = "__all__"


class TeamCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = (
            "name",
            "description",
            "motto",
        )
