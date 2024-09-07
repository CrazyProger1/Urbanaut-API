from rest_framework import viewsets, generics, mixins, permissions

from src.apps.abandoned.serializers import AreaListSerializer, AreaRetrieveSerializer
from src.apps.abandoned.services import get_all_areas


class AreaViewSet(
    viewsets.GenericViewSet,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
):
    queryset = get_all_areas()
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    serializer_class = AreaListSerializer

    def get_serializer_class(self):
        match self.action:
            case "list":
                return AreaListSerializer
            case "retrieve":
                return AreaRetrieveSerializer
        return self.serializer_class
