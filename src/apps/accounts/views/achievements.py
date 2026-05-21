from rest_framework import viewsets, mixins, permissions

from src.apps.accounts.serializers import (
    TeamListSerializer,
    TeamCreateSerializer,
    TeamRetrieveSerializer,
    AchievementRetrieveSerializer,
)
from src.apps.accounts.services.db import get_all_teams, get_all_achievements
from src.utils.django.views import MultipleSerializerViewsetMixin


class AchievementViewSet(
    MultipleSerializerViewsetMixin,
    viewsets.GenericViewSet,
    mixins.RetrieveModelMixin,
):
    queryset = get_all_achievements()
    serializer_class = AchievementRetrieveSerializer
    serializer_classes = {
        "retrieve": AchievementRetrieveSerializer,
    }
    lookup_field = "slug"
