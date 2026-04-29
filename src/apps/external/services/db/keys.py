from src.apps.external.models import Key


def get_key_or_none(pk: str) -> Key | None:
    return Key.objects.filter(pk=pk).first()
