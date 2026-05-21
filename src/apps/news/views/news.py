from rest_framework import viewsets, mixins, filters

from src.apps.news.serializers import NewsListSerializer, NewsRetrieveSerializer
from src.apps.news.services.db import get_published_news
from src.utils.django.views import MultipleSerializerViewsetMixin


class NewsViewSet(
    MultipleSerializerViewsetMixin,
    viewsets.GenericViewSet,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
):
    queryset = get_published_news()
    serializer_class = NewsListSerializer
    serializer_classes = {
        "list": NewsListSerializer,
        "retrieve": NewsRetrieveSerializer,
    }
    filter_backends = (filters.OrderingFilter,)
    ordering_fields = ("published_at",)
