from rest_framework import viewsets, mixins
from rest_framework.permissions import IsAuthenticated

from src.apps.accounts.serializers import (
    SettingsUpdateSerializer,
    SettingsRetrieveSerializer,
)
from src.apps.accounts.services.db import get_all_settings


class SettingsViewSet(
    viewsets.GenericViewSet,
    mixins.UpdateModelMixin,
    mixins.RetrieveModelMixin,
):
    queryset = get_all_settings()
    permission_classes = (IsAuthenticated,)
    serializer_class = SettingsRetrieveSerializer
    serializer_classes = {
        "update": SettingsUpdateSerializer,
        "partial_update": SettingsUpdateSerializer,
        "retrieve": SettingsRetrieveSerializer,
    }

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action, self.serializer_class)

    def get_object(self):
        return self.request.user.settings
