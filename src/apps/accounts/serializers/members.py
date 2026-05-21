from rest_framework import serializers

from src.apps.accounts.models import TeamMember
from src.apps.accounts.serializers import UserListSerializer


class TeamMemberListSerializer(serializers.ModelSerializer):
    user = UserListSerializer(source="member", read_only=True)

    class Meta:
        model = TeamMember
        fields = (
            "id",
            "user",
            "team",
        )
