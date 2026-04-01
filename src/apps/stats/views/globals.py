from drf_spectacular.utils import extend_schema
from rest_framework import views, response, status

from src.apps.abandoned.services.db import count_places, count_areas
from src.apps.accounts.services.db import count_users
from src.apps.expeditions.services.db import count_expeditions
from src.apps.geo.services.db import count_active_countries
from src.apps.stats.serializers import GlobalStatsRetrieveSerializer


class GlobalStatsView(views.APIView):

    @extend_schema(
        responses=GlobalStatsRetrieveSerializer,
    )
    def get(self, request, **kwargs):
        serializer = GlobalStatsRetrieveSerializer(instance={
            "places_count": count_places(),
            "areas_count": count_areas(),
            "users_count": count_users(),
            "countries_count": count_active_countries(),
            "expeditions_count": count_expeditions(),
        })
        return response.Response(serializer.data, status=status.HTTP_200_OK)
