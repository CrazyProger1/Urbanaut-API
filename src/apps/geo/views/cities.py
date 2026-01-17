from django_filters import rest_framework as filters
from rest_framework import viewsets, mixins

from src.apps.geo.filters import CityFilter
from src.apps.geo.serializers import CityListSerializer

from src.apps.geo.services.db import get_active_cities


class CityViewSet(viewsets.GenericViewSet, mixins.ListModelMixin):
    queryset = get_active_cities()
    serializer_class = CityListSerializer
    filterset_class = CityFilter
    filter_backends = (filters.DjangoFilterBackend,)
