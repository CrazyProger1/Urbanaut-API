from rest_framework import viewsets, mixins

from src.apps.feedbacks.serializers import (
    FeedbackCreateSerializer,
    RequestCreateSerializer,
)
from src.apps.feedbacks.services.db import get_all_feedbacks, get_all_requests


class RequestViewSet(viewsets.GenericViewSet, mixins.CreateModelMixin):
    queryset = get_all_requests()
    serializer_class = RequestCreateSerializer

    def perform_create(self, serializer):
        user = self.request.user

        if user.is_authenticated:
            serializer.save(requested_by=user)
        else:
            serializer.save()
