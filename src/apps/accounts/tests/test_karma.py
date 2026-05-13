import pytest

from src.apps.accounts.models import User, KarmaTransaction


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