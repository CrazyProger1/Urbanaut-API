import pytest

from src.apps.finances.models import Balance, Transaction
from src.apps.finances.services.finances import (
    make_transaction,
    make_system_transaction,
)


@pytest.fixture
def balance_in():
    return Balance.objects.create()


@pytest.fixture
def balance_out():
    return Balance.objects.create()


@pytest.fixture
def pool():
    return Balance.objects.create(is_pool=True)


@pytest.mark.django_db
@pytest.mark.parametrize(
    "amount",
    [
        100,
        1000,
        100000,
        1,
    ],
)
def test_make_transaction(amount: int, balance_in, balance_out, pool) -> None:
    Transaction.objects.create(amount=amount, balance_in=balance_out, balance_out=pool)

    transaction = make_transaction(
        amount=amount, balance_out=balance_out, balance_in=balance_in
    )

    assert transaction.amount == amount
    assert transaction.balance_in == balance_in
    assert transaction.balance_out == balance_out


@pytest.mark.django_db
@pytest.mark.parametrize(
    "amount",
    [
        -100,
        -1,
        0,
    ],
)
def test_make_transaction_negative_or_zero(
    amount: int, balance_in, balance_out
) -> None:
    with pytest.raises(ValueError):
        make_transaction(amount=amount, balance_out=balance_out, balance_in=balance_in)


@pytest.mark.django_db
@pytest.mark.parametrize(
    "amount",
    [
        1000,
        1,
        -1000,
        -1,
    ],
)
def test_make_system_transaction(amount: int, balance_in, pool) -> None:
    transaction = make_system_transaction(amount=amount, balance=balance_in)

    assert transaction.amount == abs(amount)

    if amount < 0:
        assert transaction.balance_out == balance_in
    else:
        assert transaction.balance_in == balance_in
