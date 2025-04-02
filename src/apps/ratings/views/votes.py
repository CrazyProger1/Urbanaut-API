from rest_framework import viewsets, mixins, permissions

from src.apps.ratings.serializers import RatingVoteCreateSerializer
from src.apps.ratings.services.db import get_all_votes


class RatingVoteViewSet(
    viewsets.GenericViewSet,
    mixins.CreateModelMixin,
):
    serializer_class = RatingVoteCreateSerializer
    queryset = get_all_votes()
    permission_classes = (permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)
