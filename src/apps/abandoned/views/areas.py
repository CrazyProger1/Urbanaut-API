from rest_framework import viewsets, mixins
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from src.apps.abandoned.services.db import get_all_areas
from src.apps.abandoned.serializers import (
    AreaRetrieveSerializer,
    AreaListSerializer,
)
from src.utils.django.views import MultipleSerializerViewsetMixin


class AreaViewSet(
    MultipleSerializerViewsetMixin,
    viewsets.GenericViewSet,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
):
    queryset = get_all_areas()
    permission_classes = (IsAuthenticatedOrReadOnly,)
    serializer_class = AreaRetrieveSerializer
    serializer_classes = {
        "list": AreaListSerializer,
        "retrieve": AreaRetrieveSerializer,
    }

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)
