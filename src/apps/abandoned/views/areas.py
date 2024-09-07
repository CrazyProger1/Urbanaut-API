from rest_framework import viewsets, generics, mixins, permissions

from src.apps.abandoned.serializers import (
    AbandonedAreaListSerializer,
    AbandonedAreaRetrieveSerializer,
)
from src.apps.abandoned.services import get_all_abandoned_areas


class AbandonedAreaViewSet(
    viewsets.GenericViewSet,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
):
    queryset = get_all_abandoned_areas()
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    serializer_class = AbandonedAreaListSerializer

    def get_serializer_class(self):
        match self.action:
            case "list":
                return AbandonedAreaListSerializer
            case "retrieve":
                return AbandonedAreaRetrieveSerializer
        return self.serializer_class
