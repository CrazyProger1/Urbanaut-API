from rest_framework import viewsets, mixins, permissions

from src.apps.abandoned.serializers import (
    AbandonedAreaListSerializer,
    AbandonedAreaRetrieveSerializer,
)
from src.apps.abandoned.services.db import get_available_abandoned_areas
from src.apps.permissions.permissions import HasPermission


class AbandonedAreaViewSet(
    viewsets.GenericViewSet,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
):
    queryset = get_available_abandoned_areas()
    permission_classes = (HasPermission,)
    serializer_class = AbandonedAreaListSerializer
    serializer_classes = {
        "list": AbandonedAreaListSerializer,
        "retrieve": AbandonedAreaRetrieveSerializer,
    }

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return get_available_abandoned_areas(user=self.request.user)

        return self.queryset

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action, self.serializer_class)
