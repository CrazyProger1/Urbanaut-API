from rest_framework import viewsets, mixins, permissions

from src.apps.abandoned.serializers import (
    AbandonedObjectListSerializer,
    AbandonedObjectRetrieveSerializer,
)
from src.apps.abandoned.services import get_all_abandoned_objects


class AbandonedObjectViewSet(
    viewsets.GenericViewSet,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
):
    queryset = get_all_abandoned_objects()
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    serializer_class = AbandonedObjectListSerializer

    def get_serializer_class(self):
        match self.action:
            case "list":
                return AbandonedObjectListSerializer
            case "retrieve":
                return AbandonedObjectRetrieveSerializer
        return self.serializer_class
