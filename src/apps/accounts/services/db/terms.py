from src.apps.accounts.models import Terms
from src.utils.db import get_all_objects, filter_objects


def get_all_terms():
    return get_all_objects(source=Terms)


def get_current_terms() -> Terms:
    return filter_objects(source=Terms, is_active=True).order_by("-created_at").first()
