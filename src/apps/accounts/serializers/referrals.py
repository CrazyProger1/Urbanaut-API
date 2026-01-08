from rest_framework import serializers

from src.apps.accounts.models import ReferralCode


class ReferralCodeRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReferralCode
        fields = ("code",)


class ReferralCodeListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReferralCode
        fields = ("code",)
