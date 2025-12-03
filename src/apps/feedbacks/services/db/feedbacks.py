from django.db import models

from src.apps.feedbacks.models import Feedback


def get_all_feedbacks() -> models.QuerySet[Feedback]:
    return Feedback.objects.all()
