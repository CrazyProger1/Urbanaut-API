import logging

from django.db import transaction

from src.apps.finances.models import Balance, Transaction
from src.apps.finances.services.db import get_system_pool

logger = logging.getLogger(__name__)


@transaction.atomic
def make_transaction(amount: int, balance_out: Balance, balance_in: Balance) -> Transaction:
    if amount < 0:
        raise ValueError("Amount cannot be negative. Change in/out balances")
    elif amount == 0:
        raise ValueError("Amount cannot be zero")

    logger.info("Performing transaction (%s): %s -> %s", amount, balance_in.pk, balance_out.pk)
    transaction = Transaction.objects.create(amount=amount, balance_out=balance_out, balance_in=balance_in)
    logger.info(
        "Transaction (%s, %s) performed: %s -> %s",
        amount,
        transaction.signature,
        balance_in.pk,
        balance_out.pk,
    )
    return transaction


@transaction.atomic
def make_system_transaction(amount: int, balance: Balance, pool: Balance = None) -> Transaction:
    if not pool:
        pool = get_system_pool()

    is_out = amount < 0
    kwargs = {
        "amount": abs(amount),
        "balance_in": balance,
        "balance_out": pool,
    }

    if is_out:
        kwargs["balance_out"] = balance
        kwargs["balance_in"] = pool

    return make_transaction(
        **kwargs,
    )
