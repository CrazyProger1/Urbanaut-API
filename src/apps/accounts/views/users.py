from rest_framework import viewsets, mixins, permissions

from src.apps.accounts.filters import UserFilter
from src.apps.accounts.serializers import UserListSerializer, UserRetrieveSerializer
from src.apps.accounts.services.db import get_active_users


class UserViewSet(
    viewsets.GenericViewSet,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
):
    queryset = get_active_users()
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    serializer_class = UserListSerializer
    filterset_class = UserFilter

    def get_serializer_class(self):
        match self.action:
            case "list":
                return UserListSerializer
            case "retrieve":
                return UserRetrieveSerializer
        return self.serializer_class
