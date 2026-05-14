import pytest

from src.apps.accounts.models import User, KarmaTransaction
from src.apps.accounts.services.db.karma import make_karma_transaction


@pytest.fixture
def user(db):
    return User.objects.create_user(email="test@example.com", password="pass")


@pytest.mark.django_db
class TestUserKarma:
    def test_no_transactions_returns_none(self, user):
        assert user.karma is None

    def test_single_positive_transaction(self, user):
        KarmaTransaction.objects.create(user=user, amount=10)
        assert user.karma == 10

    def test_single_negative_transaction(self, user):
        KarmaTransaction.objects.create(user=user, amount=-5)
        assert user.karma == -5

    def test_multiple_transactions_summed(self, user):
        KarmaTransaction.objects.create(user=user, amount=20)
        KarmaTransaction.objects.create(user=user, amount=-8)
        assert user.karma == 12

    def test_zero_amount_transaction(self, user):
        KarmaTransaction.objects.create(user=user, amount=0)
        assert user.karma == 0

    def test_only_counts_own_transactions(self, user, db):
        other = User.objects.create_user(email="other@example.com", password="pass")
        KarmaTransaction.objects.create(user=other, amount=50)
        assert user.karma is None


@pytest.mark.django_db
class TestMakeKarmaTransaction:
    def test_creates_transaction(self, user):
        tx = make_karma_transaction(user=user, amount=10)
        assert tx.pk is not None
        assert tx.user == user
        assert tx.amount == 10

    def test_negative_amount(self, user):
        tx = make_karma_transaction(user=user, amount=-5)
        assert tx.amount == -5

    def test_zero_raises(self, user):
        with pytest.raises(ValueError):
            make_karma_transaction(user=user, amount=0)

    def test_persisted_to_db(self, user):
        make_karma_transaction(user=user, amount=10)
        assert KarmaTransaction.objects.filter(user=user).count() == 1

    def test_float_amount_cast_to_int(self, user):
        tx = make_karma_transaction(user=user, amount=7.9)
        assert tx.amount == 7