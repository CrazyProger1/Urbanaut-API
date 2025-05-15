from django.contrib.auth import get_user_model
from rest_framework import serializers

from src.apps.accounts.serializers.ranks import RankListSerializer
from src.apps.accounts.serializers.settings import SettingsRetrieveSerializer
from src.apps.accounts.services.db import is_friend, count_friends

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
    is_friend = serializers.SerializerMethodField(read_only=True)
    friends_count = serializers.SerializerMethodField(read_only=True)

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
            "is_friend",
            "friends_count",
        )

    def get_avatar(self, obj: User) -> str | None:
        return obj.avatar.src if obj.avatar else None

    def get_friends_count(self, obj: User) -> int:
        return count_friends(user=obj)

    def get_is_friend(self, obj: User) -> bool | None:
        request = self.context.get("request", None)

        if request and request.user.is_authenticated:
            user = request.user

            if user == obj:
                return False

            return is_friend(
                user=user,
                friend=obj,
            )

        return False
