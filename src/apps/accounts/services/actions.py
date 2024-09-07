from src.apps.accounts.models import UserAction
from src.utils.db import create_object


def create_action(**data):
    return create_object(UserAction, **data)
