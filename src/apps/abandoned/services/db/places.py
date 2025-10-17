from src.apps.abandoned.models import Place


def get_all_places():
    return Place.objects.all()
