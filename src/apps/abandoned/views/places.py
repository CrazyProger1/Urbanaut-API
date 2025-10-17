from rest_framework import viewsets, mixins
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from src.apps.abandoned.services.db import get_all_places
from src.apps.abandoned.serializers import (
    PlaceRetrieveSerializer,
    PlaceListSerializer,
    PlaceCreateSerializer

)
from src.utils.django.views import MultipleSerializerViewsetMixin


class PlaceViewSet(
    MultipleSerializerViewsetMixin,
    viewsets.GenericViewSet,
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
):
    queryset = get_all_places()
    permission_classes = (IsAuthenticatedOrReadOnly,)
    serializer_class = PlaceRetrieveSerializer
    serializer_classes = {
        "list": PlaceListSerializer,
        "retrieve": PlaceRetrieveSerializer,
        "create": PlaceCreateSerializer,
    }

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)
