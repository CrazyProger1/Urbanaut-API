from rest_framework import viewsets, mixins, permissions, serializers
from django_filters import rest_framework as filters

from src.apps.abandoned.filters import AbandonedObjectFilter
from src.apps.abandoned.serializers import (
    AbandonedObjectListSerializer,
    AbandonedObjectRetrieveSerializer,
    AbandonedObjectCreateSerializer,
)
from src.apps.abandoned.services import get_unhidden_abandoned_objects
from src.utils.filters import DistanceBackend


class AbandonedObjectViewSet(
    viewsets.GenericViewSet,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
):
    queryset = get_unhidden_abandoned_objects()
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    serializer_class = AbandonedObjectListSerializer
    point_field = "location__point"
    filter_backends = (
        filters.DjangoFilterBackend,
        DistanceBackend,
    )
    filterset_class = AbandonedObjectFilter

    def get_serializer_class(self):
        match self.action:
            case "list":
                return AbandonedObjectListSerializer
            case "retrieve":
                return AbandonedObjectRetrieveSerializer
            case "create":
                return AbandonedObjectCreateSerializer
        return self.serializer_class

    def perform_create(self, serializer: serializers.Serializer):
        serializer.save(
            creator=self.request.from_user,
            is_hidden=True,
        )
