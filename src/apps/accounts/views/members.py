from django_filters import rest_framework as filters
from rest_framework import viewsets, mixins, permissions

from src.apps.accounts.filters import TeamMemberFilter
from src.apps.accounts.serializers.members import TeamMemberListSerializer
from src.apps.accounts.services.db import get_all_team_members


class TeamMemberViewSet(
    viewsets.GenericViewSet,
    mixins.ListModelMixin,
):
    queryset = get_all_team_members()
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    serializer_class = TeamMemberListSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = TeamMemberFilter