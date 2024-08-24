from src.apps.abandoned.models import AbandonedObject


def get_all_objects():
    return AbandonedObject.objects.all()
