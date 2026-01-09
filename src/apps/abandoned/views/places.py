from django_filters import rest_framework as filters
from rest_framework import viewsets, mixins, exceptions
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
from src.apps.geo.services.db import is_country_supported
from src.apps.geo.services.geocoding import try_convert_geocoding_address_to_database_address
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
        user = self.request.user
        if user.is_authenticated and user.is_superuser:
            return self.queryset
        return get_user_or_public_places(user=self.request.user)

    def perform_create(self, serializer):
        point = serializer.validated_data["point"]
        address = reverse_geocode((point.y, point.x))
        db_address = try_convert_geocoding_address_to_database_address(address=address, new=True)
        country = db_address.country

        if country and not is_country_supported(country=country):
            raise exceptions.PermissionDenied(detail="Country not supported")

        if not db_address:
            raise exceptions.PermissionDenied(detail="Address not exists")

        instance = serializer.save(created_by=self.request.user)
        area = get_place_area_or_none(place=instance)

        if area:
            instance.area = area
            instance.address = db_address
            instance.save(update_fields=("area",))
