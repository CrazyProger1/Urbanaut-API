from src.apps.notifier.models import Newsletter
from src.utils.db import get_object_or_none


def get_newsletter_or_none(*args, **kwargs):
    return get_object_or_none(source=Newsletter, *args, **kwargs)
