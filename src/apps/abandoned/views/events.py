from rest_framework import viewsets, mixins

from src.apps.abandoned.serializers import (
    EventListSerializer,
    EventRetrieveSerializer,
)
from src.apps.abandoned.services.db import get_available_events
from src.apps.permissions.permissions import HasPermission


class EventViewSet(
    viewsets.GenericViewSet,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
):
    queryset = get_available_events()
    permission_classes = (HasPermission,)
    serializer_class = EventListSerializer
    serializer_classes = {
        "list": EventListSerializer,
        "retrieve": EventRetrieveSerializer,
    }

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return get_available_events(user=self.request.user)

        return self.queryset

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action, self.serializer_class)
