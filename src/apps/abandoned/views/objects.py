import logging

from rest_framework import viewsets, mixins, serializers
from django_filters import rest_framework as filters

from src.apps.abandoned.filters import AbandonedObjectFilter
from src.apps.abandoned.serializers import (
    AbandonedObjectListSerializer,
    AbandonedObjectRetrieveSerializer,
    AbandonedObjectCreateSerializer,
)
from src.apps.abandoned.services.db import get_available_abandoned_objects
from src.apps.permissions.permissions import HasPermission
from src.utils.filters import DistanceBackend


class AbandonedObjectViewSet(
    viewsets.GenericViewSet,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
):
    queryset = get_available_abandoned_objects()
    permission_classes = (HasPermission,)
    serializer_class = AbandonedObjectListSerializer
    serializer_classes = {
        "list": AbandonedObjectListSerializer,
        "create": AbandonedObjectCreateSerializer,
        "retrieve": AbandonedObjectRetrieveSerializer,
    }
    point_field = "location__point"
    filter_backends = (
        filters.DjangoFilterBackend,
        DistanceBackend,
    )
    filterset_class = AbandonedObjectFilter

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action, self.serializer_class)

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return get_available_abandoned_objects(user=self.request.user)

        return self.queryset

    def perform_create(self, serializer: serializers.Serializer):
        serializer.save(
            created_by=self.request.user,
        )
