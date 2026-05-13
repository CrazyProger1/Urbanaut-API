import logging

from src.apps.accounts.models import User, KarmaTransaction

logger = logging.getLogger(__name__)


def make_karma_transaction(user: User, amount: int) -> KarmaTransaction:
    if amount == 0:
        raise ValueError("Amount cannot be zero")

    logger.info("Creating karma transaction for user %s: amount=%s", user.pk, amount)
    return KarmaTransaction.objects.create(
        user=user,
        amount=int(amount),
    )
