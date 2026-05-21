from django_filters import rest_framework as filters
from rest_framework import viewsets, mixins, permissions

from src.apps.accounts.events import TeamEventChannel, TeamCreatedEvent
from src.apps.accounts.filters import TeamFilter
from src.apps.accounts.serializers import (
    TeamListSerializer,
    TeamCreateSerializer,
    TeamRetrieveSerializer,
)
from src.apps.accounts.services.db import get_all_teams, add_creator_as_member
from src.utils.django.views import MultipleSerializerViewsetMixin


class TeamViewSet(
    MultipleSerializerViewsetMixin,
    viewsets.GenericViewSet,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
):
    queryset = get_all_teams()
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    serializer_class = TeamListSerializer
    serializer_classes = {
        "list": TeamListSerializer,
        "create": TeamCreateSerializer,
        "retrieve": TeamRetrieveSerializer,
    }
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = TeamFilter

    def perform_create(self, serializer):
        team = serializer.save(created_by=self.request.user)
        add_creator_as_member(team=team)
        TeamEventChannel.team_created.publish(event=TeamCreatedEvent(team=team))
