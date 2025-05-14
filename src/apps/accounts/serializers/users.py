from django.contrib.auth import get_user_model
from rest_framework import serializers

from src.apps.accounts.serializers.ranks import RankListSerializer
from src.apps.accounts.serializers.settings import SettingsRetrieveSerializer

User = get_user_model()


class UserListSerializer(serializers.ModelSerializer):
    rank = RankListSerializer(read_only=True)
    avatar = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = (
            "id",
            "username",
            "rank",
            "nickname",
            "avatar",
        )

    def get_avatar(self, obj: User) -> str | None:
        return obj.avatar.src if obj.avatar else None


class UserRetrieveSerializer(serializers.ModelSerializer):
    avatar = serializers.SerializerMethodField()
    rank = RankListSerializer(read_only=True)
    settings = SettingsRetrieveSerializer(read_only=True)

    class Meta:
        model = User
        fields = (
            "id",
            "username",
            "nickname",
            "first_name",
            "last_name",
            "rank",
            "experience",
            "karma",
            "last_login",
            "joined_at",
            "avatar",
            "settings",
        )

    def get_avatar(self, obj: User) -> str | None:
        return obj.avatar.src if obj.avatar else None
