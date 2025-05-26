from rest_framework import serializers

from src.apps.ratings.models import Rating
from src.apps.ratings.services.db import get_user_vote_or_none


class RatingRetrieveSerializer(serializers.ModelSerializer):
    vote = serializers.SerializerMethodField(method_name="get_user_vote")

    class Meta:
        model = Rating
        fields = (
            "id",
            "value",
            "vote",
        )

    def get_user_vote(self, obj: Rating):
        if request := self.context.get("request"):
            if user := getattr(request, "user", None):
                if user.is_authenticated:
                    if vote := get_user_vote_or_none(user, obj):
                        return vote.value
