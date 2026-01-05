from rest_framework import viewsets, mixins

from src.apps.geo.serializers import CountryListSerializer

from src.apps.geo.services.db import get_active_countries


class CountryViewSet(viewsets.GenericViewSet, mixins.ListModelMixin):
    queryset = get_active_countries()
    serializer_class = CountryListSerializer
