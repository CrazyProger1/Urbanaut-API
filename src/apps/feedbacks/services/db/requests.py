from django.utils import timezone

from src.apps.feedbacks.models import Request


def get_all_requests():
    return Request.objects.all()


def mark_request_fulfilled(request: Request, user):
    request.is_fulfilled = True
    request.fulfilled_by = user
    request.fulfilled_at = timezone.now()
    request.save()
