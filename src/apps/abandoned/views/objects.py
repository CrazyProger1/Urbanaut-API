from rest_framework import viewsets, mixins, permissions, serializers

from src.apps.abandoned.serializers import (
    AbandonedObjectListSerializer,
    AbandonedObjectRetrieveSerializer,
    AbandonedObjectCreateSerializer,
)
from src.apps.abandoned.services import get_unhidden_abandoned_objects
from src.apps.accounts.enums import UserActionType
from src.apps.accounts.services import create_action


class AbandonedObjectViewSet(
    viewsets.GenericViewSet,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
):
    queryset = get_unhidden_abandoned_objects()
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    serializer_class = AbandonedObjectListSerializer

    def get_serializer_class(self):
        match self.action:
            case "list":
                return AbandonedObjectListSerializer
            case "retrieve":
                return AbandonedObjectRetrieveSerializer
            case "create":
                return AbandonedObjectCreateSerializer
        return self.serializer_class

    def add_action(self, instance, object_updated: bool = False):
        create_action(
            type=(
                UserActionType.UPDATED_ABANDONED_OBJECT
                if object_updated
                else UserActionType.CREATED_ABANDONED_OBJECT
            ),
            user=self.request.user,
            data={
                "object": instance.id,
                "name": instance.name,
            },
        )

    def perform_create(self, serializer: serializers.Serializer):
        instance = serializer.save(
            creator=self.request.user,
            is_hidden=True,
        )
        self.add_action(instance=instance)
