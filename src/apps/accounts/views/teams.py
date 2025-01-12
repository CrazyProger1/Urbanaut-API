from rest_framework import viewsets, mixins, permissions

from src.apps.accounts.serializers import TeamListSerializer, UserRetrieveSerializer
from src.apps.accounts.services.db import get_all_teams


class TeamViewSet(
    viewsets.GenericViewSet,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
):
    queryset = get_all_teams()
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    serializer_class = TeamListSerializer

    def get_serializer_class(self):
        match self.action:
            case "list":
                return TeamListSerializer
            case "retrieve":
                return UserRetrieveSerializer
        return self.serializer_class
