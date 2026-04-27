from dataclasses import dataclass

from src.apps.accounts.models import User


@dataclass
class UserCreatedEvent:
    user: User
