from rest_framework import viewsets, mixins
from rest_framework.permissions import IsAuthenticated
from django_filters import rest_framework as filters

from src.apps.notifications.filters import NotificationFilter
from src.apps.notifications.serializers import NotificationListSerializer
from src.apps.notifications.services.db import (
    get_all_notifications,
    get_user_notifications,
)


class NotificationViewSet(
    viewsets.GenericViewSet,
    mixins.ListModelMixin,
):
    queryset = get_all_notifications()
    permission_classes = (IsAuthenticated,)
    serializer_class = NotificationListSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = NotificationFilter

    def get_queryset(self):
        return get_user_notifications(user=self.request.user)
