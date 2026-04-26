from dataclasses import dataclass

from src.apps.abandoned.models import Place
from src.apps.accounts.models import User


@dataclass
class PlaceCreatedEvent:
    created_by: User
    place: Place
