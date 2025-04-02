from rest_framework import viewsets, mixins

from src.apps.ratings.serializers import RatingRetrieveSerializer
from src.apps.ratings.services.db import get_all_ratings


class RatingViewSet(
    viewsets.GenericViewSet,
    mixins.RetrieveModelMixin,
):
    serializer_class = RatingRetrieveSerializer
    queryset = get_all_ratings()
