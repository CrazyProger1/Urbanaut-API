import logging

from src.apps.accounts.models import User, ExperienceTransaction

logger = logging.getLogger(__name__)


def make_experience_transaction(user: User, amount: int) -> ExperienceTransaction:
    if amount <= 0:
        raise ValueError("Amount must be greater than 0")

    logger.info(
        "Creating experience transaction for user %s: amount=%s", user.pk, amount
    )
    return ExperienceTransaction.objects.create(
        user=user,
        amount=int(amount),
    )
