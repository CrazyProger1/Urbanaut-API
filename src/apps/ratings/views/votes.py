import logging

from rest_framework import (
    viewsets,
    mixins,
    permissions,
    response,
    status,
    exceptions,
)

from src.apps.ratings.serializers import RatingVoteCreateSerializer
from src.apps.ratings.services.db import (
    get_all_votes,
    get_rating_or_none,
    get_rating_vote_or_none,
    update_rating_average,
)

logger = logging.getLogger(__name__)


class RatingVoteViewSet(
    viewsets.GenericViewSet,
    mixins.CreateModelMixin,
):
    serializer_class = RatingVoteCreateSerializer
    queryset = get_all_votes()
    permission_classes = (permissions.IsAuthenticated,)

    def perform_create_or_update(self, serializer, rating):
        user = self.request.user
        vote = get_rating_vote_or_none(
            created_by=user,
            rating=rating,
        )

        if vote:
            vote.value = serializer.validated_data["value"]
            vote.save(update_fields=("value",))
        else:
            serializer.save(
                created_by=user,
                rating=rating,
            )

    def get_rating(self):
        rating_pk = self.kwargs.get("rating_pk")
        if not rating_pk:
            raise exceptions.ValidationError(detail="Rating ID is required")

        rating = get_rating_or_none(pk=rating_pk)
        if not rating:
            logger.warning("Rating not found: %s", rating_pk)
            raise exceptions.NotFound(detail="Rating not found")

        return rating

    def create(self, request, *args, **kwargs):
        rating = self.get_rating()
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create_or_update(serializer, rating=rating)
        average = update_rating_average(rating=rating)
        return response.Response(
            {"value": average},
            status=status.HTTP_200_OK,
        )
