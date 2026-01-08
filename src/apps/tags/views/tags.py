from rest_framework import mixins, viewsets

from src.apps.tags.serializers import TagRetrieveSerializer, TagListSerializer
from src.apps.tags.services.db.tags import get_all_tags


class TagViewSet(
    viewsets.GenericViewSet,
    mixins.ListModelMixin,
):
    queryset = get_all_tags()
    serializer_class = TagRetrieveSerializer
    serializer_classes = {
        "retrieve": TagRetrieveSerializer,
        "list": TagListSerializer,
    }

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action, self.serializer_class)
