from django.conf import settings

from src.apps.abandoned.models import Place
from src.apps.accounts.models import User
from src.apps.finances.services.finances import make_system_transaction


def top_up_user_balance_by_place_creation(user: User, place: Place):
    make_system_transaction(
        amount=settings.REWARDS["PLACE_CREATION"],
        balance=user.balance,
    )


def give_user_achievement_by_place_creation(user: User, place: Place):
    pass
