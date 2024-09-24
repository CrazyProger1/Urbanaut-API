from src.utils.db import create_object
from src.apps.actions.models import Action


def create_action(**data):
    return create_object(Action, **data)
