from django.conf import settings
from django_filters import rest_framework as filters
from rest_framework import viewsets, mixins, response, status, exceptions
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from src.apps.abandoned.filters import PlaceFilter
from src.apps.abandoned.services.db import (
    get_all_places,
    get_place_area_or_none,
    get_user_or_public_places,
)
from src.apps.abandoned.serializers import (
    PlaceRetrieveSerializer,
    PlaceListSerializer,
    PlaceCreateSerializer,
)
from src.utils.django.views import MultipleSerializerViewsetMixin
from src.utils.geo import reverse_geocode


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
    filterset_class = PlaceFilter
    filter_backends = (filters.DjangoFilterBackend,)

    def get_queryset(self):
        return get_user_or_public_places(user=self.request.user)

    def perform_create(self, serializer):
        # TODO: use reverse geocoding for determining place address

        point = serializer.validated_data["point"]
        address = reverse_geocode((point.y, point.x))

        if address.get("country_code") not in settings.SUPPORTED_COUNTRIES:
            raise exceptions.PermissionDenied(detail="Country not supported")

        instance = serializer.save(created_by=self.request.user)
        area = get_place_area_or_none(place=instance)
        if area:
            instance.area = area
            instance.save(update_fields=("area",))
