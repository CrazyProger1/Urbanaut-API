from rest_framework import viewsets, mixins, permissions

from src.apps.accounts.serializers import (
    TeamListSerializer,
    TeamCreateSerializer,
    TeamRetrieveSerializer,
)
from src.apps.accounts.services.db import get_all_teams
from src.utils.django.views import MultipleSerializerViewsetMixin


class TeamViewSet(
    MultipleSerializerViewsetMixin,
    viewsets.GenericViewSet,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
):
    queryset = get_all_teams()
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = TeamListSerializer
    serializer_classes = {
        "list": TeamListSerializer,
        "create": TeamCreateSerializer,
        "retrieve": TeamRetrieveSerializer,
    }

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)
