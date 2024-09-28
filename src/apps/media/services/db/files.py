from src.apps.media.models import File
from src.utils.db import get_all_objects


def get_all_files():
    return get_all_objects(File)
