from src.apps.accounts.models import Terms


def get_all_terms():
    return Terms.objects.all()


def get_current_terms() -> Terms:
    return Terms.objects.filter(is_active=True).order_by("-created_at").first()
