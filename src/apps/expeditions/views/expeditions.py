from rest_framework import viewsets, mixins
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from src.apps.expeditions.serializers import (
    ExpeditionListSerializer,
    ExpeditionRetrieveSerializer,
    ExpeditionCreateSerializer,
)
from src.apps.expeditions.services.db import get_all_expeditions
from src.utils.django.views import MultipleSerializerViewsetMixin


class ExpeditionViewSet(
    MultipleSerializerViewsetMixin,
    viewsets.GenericViewSet,
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
):
    queryset = get_all_expeditions()
    permission_classes = (IsAuthenticatedOrReadOnly,)
    serializer_class = ExpeditionRetrieveSerializer
    serializer_classes = {
        "list": ExpeditionListSerializer,
        "retrieve": ExpeditionRetrieveSerializer,
        "create": ExpeditionCreateSerializer,
    }
