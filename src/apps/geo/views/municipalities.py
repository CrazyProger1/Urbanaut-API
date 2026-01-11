from rest_framework import viewsets, mixins

from src.apps.geo.serializers import MunicipalityListSerializer


class MunicipalityViewSet(viewsets.GenericViewSet, mixins.ListModelMixin):
    serializer_class = MunicipalityListSerializer
