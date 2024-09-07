from rest_framework import viewsets, mixins, permissions

from src.apps.abandoned.serializers import (
    ObjectListSerializer,
    ObjectRetrieveSerializer,
)
from src.apps.abandoned.services import get_all_objects


class ObjectViewSet(
    viewsets.GenericViewSet,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
):
    queryset = get_all_objects()
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    serializer_class = ObjectListSerializer

    def get_serializer_class(self):
        match self.action:
            case "list":
                return ObjectListSerializer
            case "retrieve":
                return ObjectRetrieveSerializer
        return self.serializer_class
