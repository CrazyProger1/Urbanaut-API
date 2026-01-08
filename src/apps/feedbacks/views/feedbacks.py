from rest_framework import viewsets, mixins

from src.apps.feedbacks.serializers import FeedbackCreateSerializer
from src.apps.feedbacks.services.db import get_all_feedbacks


class FeedbackViewSet(viewsets.GenericViewSet, mixins.CreateModelMixin):
    queryset = get_all_feedbacks()
    serializer_class = FeedbackCreateSerializer
