from rest_framework import serializers

from src.apps.ratings.models import Rating


class RatingRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = (
            "id",
            "value",
        )
