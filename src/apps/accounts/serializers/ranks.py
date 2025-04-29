from rest_framework import serializers

from src.apps.accounts.models import Rank


class RankListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rank
        fields = (
            "id",
            "key",
            "name",
        )
