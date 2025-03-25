from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()


class UserListSerializer(serializers.ModelSerializer):
    rank = serializers.CharField(source="rank.key")

    class Meta:
        model = User
        fields = (
            "id",
            "username",
            "rank",
            "nickname",
        )


class UserRetrieveSerializer(serializers.ModelSerializer):
    avatar = serializers.SerializerMethodField()
    rank = serializers.CharField(source="rank.key")

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
        )

    def get_avatar(self, obj: User) -> str | None:
        return obj.avatar.src if obj.avatar else None
