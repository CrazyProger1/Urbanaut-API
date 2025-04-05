from rest_framework import viewsets, mixins, permissions

from src.apps.accounts.serializers import SettingsUpdateSerializer
from src.apps.accounts.services.db import get_all_settings, get_user_settings


class SettingsViewSet(
    viewsets.GenericViewSet,
    mixins.UpdateModelMixin,
):
    queryset = get_all_settings()
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = SettingsUpdateSerializer
    lookup_field = None

    def get_object(self):
        return get_user_settings(self.request.user)
