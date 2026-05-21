from django.conf import settings
from rest_framework import viewsets, mixins

from src.apps.accounts.services.achivements import give_achievement
from src.apps.feedbacks.serializers import FeedbackCreateSerializer
from src.apps.feedbacks.services.db import get_all_feedbacks


class FeedbackViewSet(viewsets.GenericViewSet, mixins.CreateModelMixin):
    queryset = get_all_feedbacks()
    serializer_class = FeedbackCreateSerializer

    def perform_create(self, serializer):
        super().perform_create(serializer=serializer)
        if self.request.user.is_authenticated:
            give_achievement(self.request.user, settings.TESTER_ACHIEVEMENT_SLUG)
