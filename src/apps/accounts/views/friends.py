from rest_framework import viewsets, mixins, permissions

from src.apps.accounts.serializers import FriendListSerializer
from src.apps.accounts.services.db import get_all_friends, get_user_friends


class FriendViewSet(
    viewsets.GenericViewSet,
    mixins.ListModelMixin,
):
    queryset = get_all_friends()
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = FriendListSerializer
    serializer_classes = {
        "list": FriendListSerializer,
    }

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action, self.serializer_class)

    def get_queryset(self):
        return get_user_friends(user=self.request.user)
