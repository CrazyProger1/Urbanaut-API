from rest_framework import viewsets, mixins, permissions, response

from src.apps.notifier.serializers import (
    NotificationListSerializer,
    NotificationRetrieveSerializer,
)
from src.apps.notifier.services.db import (
    get_user_notifications,
    get_all_notifications,
    mark_read, annotate_is_read_notifications,
)


class NotificationViewSet(
    viewsets.GenericViewSet,
    mixins.ListModelMixin,
):
    queryset = get_all_notifications()
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = NotificationListSerializer

    def get_serializer_class(self):
        match self.action:
            case "list":
                return NotificationListSerializer
            case "retrieve":
                return NotificationRetrieveSerializer
        return self.serializer_class

    def get_queryset(self):
        user = self.request.user
        return annotate_is_read_notifications(
            notifications=get_user_notifications(user=user),
            user=user,
        )

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)

        if page is not None:
            serializer = self.get_serializer(page, many=True)
            data = serializer.data
            mark_read(
                notifications=page,
                user=request.user,
            )
            return self.get_paginated_response(data)

        serializer = self.get_serializer(queryset, many=True)
        data = serializer.data
        mark_read(
            notifications=queryset,
            user=request.user,
        )
        return response.Response(data)
