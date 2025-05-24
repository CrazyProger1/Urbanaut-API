from rest_framework import serializers

from src.apps.ratings.models import RatingVote


class RatingVoteCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = RatingVote
        fields = (
            "value",
        )
