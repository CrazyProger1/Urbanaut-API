import pytest

from src.apps.finances.exceptions import BalanceOutError
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
    Transaction.objects.create(
        amount=amount,
        balance_in=balance_out,
        balance_out=pool,
    )

    transaction = make_transaction(
        amount=amount,
        balance_out=balance_out,
        balance_in=balance_in,
    )

    assert transaction.amount == amount
    assert transaction.balance_in == balance_in
    assert transaction.balance_out == balance_out
    assert balance_in.money == amount


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
        make_transaction(
            amount=amount,
            balance_out=balance_out,
            balance_in=balance_in,
        )


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
    if amount < 0:
        Transaction.objects.create(
            amount=abs(amount),
            balance_in=balance_in,
            balance_out=pool,
        )

    transaction = make_system_transaction(amount=amount, balance=balance_in)

    assert transaction.amount == abs(amount)

    if amount < 0:
        assert transaction.balance_out == balance_in
        assert transaction.balance_in == pool
        assert balance_in.money == 0
    else:
        assert transaction.balance_in == balance_in
        assert transaction.balance_out == pool
        assert balance_in.money == amount


@pytest.mark.django_db
@pytest.mark.parametrize(
    "amount",
    [
        1000,
        1,
    ],
)
def test_make_transaction_with_no_money(
        amount: int, balance_out: Balance, balance_in: Balance
) -> None:
    with pytest.raises(BalanceOutError):
        make_transaction(
            amount=amount,
            balance_out=balance_out,
            balance_in=balance_in,
        )
