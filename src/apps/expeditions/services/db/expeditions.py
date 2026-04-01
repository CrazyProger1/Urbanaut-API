from src.apps.expeditions.models import Expedition


def count_expeditions():
    return Expedition.objects.count()
