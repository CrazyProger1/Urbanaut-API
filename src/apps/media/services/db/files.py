from src.apps.media.models import File


def get_all_files():
    return File.objects.all()


def get_visible_files():
    return File.objects.filter(is_hidden=False)


def get_user_files(user):
    return File.objects.filter(created_by=user)


def create_file(**data) -> File:
    return File.objects.create(**data)
