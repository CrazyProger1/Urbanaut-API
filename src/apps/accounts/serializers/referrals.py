from rest_framework import serializers

from src.apps.accounts.models import ReferralLink


class ReferralLinkListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReferralLink
        fields = (
            "id",
            "link",
        )


class ReferralLinkRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReferralLink
        fields = (
            "id",
            "link",
        )
