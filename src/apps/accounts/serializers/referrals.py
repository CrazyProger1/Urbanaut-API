from rest_framework import serializers

from src.apps.accounts.models import ReferralLink


class ReferralLinkListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReferralLink
        fields = (
            "link",
            "code",
        )


class ReferralLinkRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReferralLink
        fields = (
            "link",
            "code",
        )


class ReferralLinkApplySerializer(serializers.Serializer):
    pass
