from django.conf import settings

from src.apps.accounts.models import User
from src.apps.finances.services.finances import make_system_transaction


def top_up_new_user_balance(user: User):
    make_system_transaction(
        amount=settings.FINANCIAL_REWARDS["NEW_USER"],
        balance=user.balance,
        destination={**settings.FINANCIAL_DESTINATION["NEW_USER"], "user_pk": user.pk},
    )
