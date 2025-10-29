from src.apps.tags.models import Tag


def get_all_tags():
    return Tag.objects.all()
