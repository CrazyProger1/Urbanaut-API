from rest_framework import viewsets, mixins, permissions

from src.apps.abandoned.serializers import (
    AbandonedObjectListSerializer,
    AbandonedObjectRetrieveSerializer, AbandonedObjectCreateSerializer,
)
from src.apps.abandoned.services import get_unhidden_abandoned_objects


class AbandonedObjectViewSet(
    viewsets.GenericViewSet,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
):
    queryset = get_unhidden_abandoned_objects()
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    serializer_class = AbandonedObjectListSerializer

    def get_serializer_class(self):
        match self.action:
            case "list":
                return AbandonedObjectListSerializer
            case "retrieve":
                return AbandonedObjectRetrieveSerializer
            case "create":
                return AbandonedObjectCreateSerializer
        return self.serializer_class

    def perform_create(self, serializer):
        serializer.save(
            creator=self.request.user,
            is_hidden=True,
        )
