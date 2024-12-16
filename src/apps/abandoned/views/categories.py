from rest_framework import viewsets, mixins

from src.apps.abandoned.serializers import (
    AbandonedObjectCategoryListSerializer,
    AbandonedObjectCategoryRetrieveSerializer,
)
from src.apps.abandoned.services.db import get_available_abandoned_object_categories
from src.apps.permissions.permissions import HasPermission


class AbandonedObjectCategoryViewSet(
    viewsets.GenericViewSet,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
):
    queryset = get_available_abandoned_object_categories()
    permission_classes = (HasPermission,)
    serializer_class = AbandonedObjectCategoryListSerializer
    serializer_classes = {
        "list": AbandonedObjectCategoryListSerializer,
        "retrieve": AbandonedObjectCategoryRetrieveSerializer,
    }

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return get_available_abandoned_object_categories(user=self.request.user)

        return self.queryset

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action, self.serializer_class)
