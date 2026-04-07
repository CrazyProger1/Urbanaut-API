from rest_framework import viewsets, mixins
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from src.apps.expeditions.serializers import (
    ReportListSerializer,
    ReportRetrieveSerializer,
    ReportCreateSerializer,
)
from src.apps.expeditions.services.db import get_all_reports
from src.utils.django.views import MultipleSerializerViewsetMixin


class ReportViewSet(
    MultipleSerializerViewsetMixin,
    viewsets.GenericViewSet,
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
):
    queryset = get_all_reports()
    permission_classes = (IsAuthenticatedOrReadOnly,)
    serializer_class = ReportRetrieveSerializer
    serializer_classes = {
        "list": ReportListSerializer,
        "retrieve": ReportRetrieveSerializer,
        "create": ReportCreateSerializer,
    }
