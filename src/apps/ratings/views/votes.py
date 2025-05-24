from rest_framework import viewsets, mixins, permissions, response, status, exceptions

from src.apps.ratings.serializers import RatingVoteCreateSerializer
from src.apps.ratings.services.db import get_all_votes, get_rating_or_none, get_rating_vote_or_none


class RatingVoteViewSet(
    viewsets.GenericViewSet,
    mixins.CreateModelMixin,
):
    serializer_class = RatingVoteCreateSerializer
    queryset = get_all_votes()
    permission_classes = (permissions.IsAuthenticated,)

    def perform_create_or_update(self, serializer):
        rating_pk = self.kwargs.get("rating_pk")
        if not rating_pk:
            raise exceptions.ValidationError(detail="Rating ID is required")

        rating = get_rating_or_none(pk=rating_pk)
        if not rating:
            raise exceptions.NotFound(detail="Rating not found")

        user = self.request.user
        vote = get_rating_vote_or_none(
            created_by=user,
            rating=rating,
        )

        if vote:
            serializer.save()
        else:
            serializer.save(
                created_by=user,
                rating=rating,
            )

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create_or_update(serializer)
        headers = self.get_success_headers(serializer.data)
        return response.Response(
            serializer.data,
            status=status.HTTP_200_OK,
            headers=headers,
        )
