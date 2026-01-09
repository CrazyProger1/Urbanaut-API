from src.apps.geo.models import Address


def create_address(**data) -> Address:
    return Address.objects.create(**data)


def get_or_create_address(**data) -> Address:
    return Address.objects.get_or_create(**data)[0]
