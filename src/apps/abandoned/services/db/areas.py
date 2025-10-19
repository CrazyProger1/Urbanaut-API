from src.apps.abandoned.models import Area


def get_all_areas():
    return Area.objects.all()