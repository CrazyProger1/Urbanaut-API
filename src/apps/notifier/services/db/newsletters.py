from django.utils import timezone

from src.apps.notifier.models import Newsletter
from src.utils.db import get_object_or_none


def get_newsletter_or_none(*args, **kwargs):
    return get_object_or_none(source=Newsletter, *args, **kwargs)


def mark_newsletter_shown(newsletter: Newsletter):
    newsletter.is_shown = True
    newsletter.shown_at = timezone.now()
    newsletter.save(update_fields=(
        "is_shown",
        "shown_at",
    ))
