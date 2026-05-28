from rest_framework import viewsets, mixins
from rest_framework.permissions import IsAuthenticated
from django_filters import rest_framework as filters

from src.apps.notifications.filters import NotificationFilter
from src.apps.notifications.serializers import (
    NotificationListSerializer,
    NotificationRetrieveSerializer,
)
from src.apps.notifications.services.db import (
    get_all_notifications,
    get_user_shown_notifications,
)
from src.utils.django.views import MultipleSerializerViewsetMixin


class NotificationViewSet(
    MultipleSerializerViewsetMixin,
    viewsets.GenericViewSet,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
):
    queryset = get_all_notifications()
    permission_classes = (IsAuthenticated,)
    serializer_class = NotificationListSerializer
    serializer_classes = {
        "list": NotificationListSerializer,
        "retrieve": NotificationRetrieveSerializer,
    }
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = NotificationFilter

    def get_queryset(self):
        return get_user_shown_notifications(user=self.request.user)
