from rest_framework import viewsets, permissions, mixins

from src.apps.geo.serializers import CountryListSerializer

from src.apps.geo.services.db import get_active_countries


class CountryViewSet(viewsets.GenericViewSet, mixins.ListModelMixin):
    queryset = get_active_countries()
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = CountryListSerializer
