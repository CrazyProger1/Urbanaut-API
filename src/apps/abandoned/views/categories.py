from rest_framework import viewsets, mixins, response
from rest_framework.decorators import action

from src.apps.abandoned.serializers import (
    AbandonedObjectCategoryListSerializer,
    AbandonedObjectCategoryRetrieveSerializer,
)
from src.apps.abandoned.services.db import (
    get_available_abandoned_object_categories,
    get_available_abandoned_object_category_children,
)
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
        return get_available_abandoned_object_categories(
            user=self.request.user
            if self.request.user.is_authenticated
            else None
        )

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action, self.serializer_class)

    @action(
        detail=True,
        methods=("GET",),
        url_name="children",
    )
    def children(self, request, *args, **kwargs):
        queryset = self.filter_queryset(
            get_available_abandoned_object_category_children(
                category=self.get_object(),
                user=request.user,
            ))

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return response.Response(serializer.data)
