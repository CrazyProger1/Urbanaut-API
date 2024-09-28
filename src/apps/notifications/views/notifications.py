from rest_framework import viewsets, mixins, permissions, response

from src.apps.notifications.serializers import (
    NotificationListSerializer,
    NotificationRetrieveSerializer,
)
from src.apps.notifications.services import (
    get_user_notifications,
    get_all_notifications,
    mark_read,
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
        return get_user_notifications(user=self.request.from_user)

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)

        if page is not None:
            serializer = self.get_serializer(page, many=True)
            mark_read(
                notifications=page,
                user=request.from_user,
            )
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        mark_read(
            notifications=queryset,
            user=request.from_user,
        )
        return response.Response(serializer.data)
