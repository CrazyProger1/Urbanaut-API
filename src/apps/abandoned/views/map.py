from django.db.models import QuerySet
from drf_spectacular.utils import extend_schema
from rest_framework import status, views, response

from src.apps.abandoned.filters import PlaceFilter
from src.apps.abandoned.models import Place
from src.apps.abandoned.serializers import MapRequestSerializer, MapResponseSerializer, serialize_place_to_geojson
from src.apps.abandoned.services.db import get_all_places


class GeoJSONMapAPIView(views.APIView):

    def serialize_places(self, places: QuerySet[Place]):
        results = []

        for place in places:
            results.append(serialize_place_to_geojson(
                place=place,
                user=self.request.user,
            ))
        return results

    def filter_places(self, queryset: QuerySet[Place]):
        params = self.request.query_params
        serializer = MapRequestSerializer(data=params)
        serializer.is_valid(raise_exception=True)
        return PlaceFilter(data=serializer.validated_data, queryset=queryset, request=self.request).qs

    @extend_schema(
        parameters=[MapRequestSerializer],
        responses={200: MapResponseSerializer},
    )
    def get(self, request, format=None):
        features = []

        features.extend(self.serialize_places(self.filter_places(queryset=get_all_places())))

        return response.Response({
            "type": "FeatureCollection",
            "features": features,
        }, status=status.HTTP_200_OK)
