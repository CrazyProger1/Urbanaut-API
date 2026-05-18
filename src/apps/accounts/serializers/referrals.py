from rest_framework import serializers

from src.apps.accounts.models import ReferralCode, Referral
from src.apps.accounts.serializers import UserListSerializer


class ReferralCodeRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReferralCode
        fields = ("code",)


class ReferralCodeListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReferralCode
        fields = ("code",)


class ReferralListSerializer(serializers.ModelSerializer):
    user = UserListSerializer(many=False, read_only=True)
    code = serializers.SlugRelatedField(slug_field="code", read_only=True)

    class Meta:
        model = Referral
        fields = (
            "code",
            "user",
        )
