from src.apps.abandoned.models import AbandonedArea


def get_all_areas():
    return AbandonedArea.objects.all()
