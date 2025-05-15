from rest_framework import serializers

from src.apps.accounts.models import Friend
from src.apps.accounts.serializers import UserListSerializer
from src.apps.accounts.services.db import get_user_friend


class FriendListSerializer(serializers.ModelSerializer):
    friend = UserListSerializer(read_only=True)

    class Meta:
        model = Friend
        fields = (
            "id",
            "friend",
            "is_approved",
            "approved_at",
        )

    def to_representation(self, instance: Friend):
        request = self.context.get("request", None)

        result = super().to_representation(instance)

        if request and request.user.is_authenticated:
            user = request.user
            friend = get_user_friend(
                user=user,
                friend=instance,
            )
            result["friend"] = UserListSerializer(friend).data

        return result
