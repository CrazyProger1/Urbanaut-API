from rest_framework import viewsets, mixins
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from src.apps.abandoned.services.db import get_all_areas, get_parent_area_or_none
from src.apps.abandoned.serializers import (
    AreaRetrieveSerializer,
    AreaListSerializer,
    AreaCreateSerializer,
)
from src.utils.django.views import MultipleSerializerViewsetMixin


class AreaViewSet(
    MultipleSerializerViewsetMixin,
    viewsets.GenericViewSet,
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
):
    queryset = get_all_areas()
    permission_classes = (IsAuthenticatedOrReadOnly,)
    serializer_class = AreaRetrieveSerializer
    serializer_classes = {
        "list": AreaListSerializer,
        "retrieve": AreaRetrieveSerializer,
        "create": AreaCreateSerializer,
    }

    def perform_create(self, serializer):
        instance = serializer.save(created_by=self.request.user)

        parent = get_parent_area_or_none(area=instance)

        if parent:
            instance.parent = parent
            instance.save(update_fields=("parent",))
