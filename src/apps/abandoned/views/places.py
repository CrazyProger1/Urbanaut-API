from django_filters import rest_framework as filters
from rest_framework import viewsets, mixins, exceptions, status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response

from src.apps.abandoned.filters import PlaceFilter
from src.apps.abandoned.pagination import DefaultUnlimitedPagination
from src.apps.abandoned.permissions import IsOwnerOrReadOnly
from src.apps.abandoned.services.db import (
    get_all_places,
    get_place_area_or_none,
    get_user_or_public_places,
    toggle_place_favorite,
    toggle_place_supposed,
)
from src.apps.abandoned.serializers import (
    PlaceRetrieveSerializer,
    PlaceListSerializer,
    PlaceCreateSerializer,
    PlaceToggleFavoriteSerializer,
    PlaceToggleSupposedSerializer,
    PlaceUpdateSerializer,
)
from src.apps.geo.services.db import is_country_supported
from src.apps.geo.services.geocoding import (
    try_convert_geocoding_address_to_database_address,
)
from src.utils.django.views import MultipleSerializerViewsetMixin
from src.utils.geo import reverse_geocode


class PlaceViewSet(
    MultipleSerializerViewsetMixin,
    viewsets.GenericViewSet,
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
):
    queryset = get_all_places()
    permission_classes = (IsAuthenticatedOrReadOnly,)
    serializer_class = PlaceRetrieveSerializer
    serializer_classes = {
        "list": PlaceListSerializer,
        "retrieve": PlaceRetrieveSerializer,
        "create": PlaceCreateSerializer,
        "update": PlaceUpdateSerializer,
        "partial_update": PlaceUpdateSerializer,
        "toggle_favorite": PlaceToggleFavoriteSerializer,
        "toggle_supposed": PlaceToggleSupposedSerializer,
    }
    filterset_class = PlaceFilter
    filter_backends = (filters.DjangoFilterBackend,)
    pagination_class = DefaultUnlimitedPagination

    def get_permissions(self):
        common = super().get_permissions()
        if self.action == "update":
            return *common, IsOwnerOrReadOnly()
        return common

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated and user.is_superuser:
            return self.queryset
        return get_user_or_public_places(user=self.request.user)

    def perform_create(self, serializer):
        point = serializer.validated_data["point"]
        address = reverse_geocode((point.y, point.x))

        if not address:
            raise exceptions.PermissionDenied(detail="Address not exists")

        db_address = try_convert_geocoding_address_to_database_address(
            address=address, point=point, new=True
        )

        if not db_address:
            raise exceptions.PermissionDenied(detail="Address not exists")

        country = db_address.country

        if country and not is_country_supported(country=country):
            raise exceptions.PermissionDenied(detail="Country not supported")

        instance = serializer.save(created_by=self.request.user)

        instance.address = db_address
        instance.area = get_place_area_or_none(place=instance)

        instance.save(update_fields=("area", "address"))

    @action(methods=["PATCH"], detail=True, url_path="toggle-favorite")
    def toggle_favorite(self, request, pk=None):
        is_favorite = toggle_place_favorite(
            place=self.get_object(),
            user=request.user,
        )

        serializer = self.get_serializer(instance={"is_favorite": is_favorite})
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(methods=["PATCH"], detail=True, url_path="toggle-supposed")
    def toggle_supposed(self, request, pk=None):
        is_supposed = toggle_place_supposed(
            place=self.get_object(),
        )

        serializer = self.get_serializer(instance={"is_supposed": is_supposed})
        return Response(serializer.data, status=status.HTTP_200_OK)
