from rest_framework import viewsets, mixins, permissions

from src.apps.ratings.serializers import RatingVoteCreateSerializer
from src.apps.ratings.services.db import get_all_votes, get_rating_or_none


class RatingVoteViewSet(
    viewsets.GenericViewSet,
    mixins.CreateModelMixin,
):
    serializer_class = RatingVoteCreateSerializer
    queryset = get_all_votes()
    permission_classes = (permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        rating = get_rating_or_none(pk=self.kwargs.get("rating_pk"))
        serializer.save(
            created_by=self.request.user,
            rating=rating,
        )
