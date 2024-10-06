from rest_framework import viewsets, generics, mixins, permissions

from src.apps.abandoned.serializers import (
    AbandonedAreaListSerializer,
    AbandonedAreaRetrieveSerializer,
)
from src.apps.abandoned.services.db import get_user_abandoned_areas, get_unhidden_abandoned_areas


class AbandonedAreaViewSet(
    viewsets.GenericViewSet,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
):
    queryset = get_unhidden_abandoned_areas()
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    serializer_class = AbandonedAreaListSerializer

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return self.queryset | get_user_abandoned_areas(user=self.request.user)

        return self.queryset

    def get_serializer_class(self):
        match self.action:
            case "list":
                return AbandonedAreaListSerializer
            case "retrieve":
                return AbandonedAreaRetrieveSerializer
        return self.serializer_class
