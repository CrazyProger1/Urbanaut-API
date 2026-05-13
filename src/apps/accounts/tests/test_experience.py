import pytest

from src.apps.accounts.models import User, ExperienceTransaction


@pytest.fixture
def user(db):
    return User.objects.create_user(email="test@example.com", password="pass")


@pytest.mark.django_db
class TestUserExperience:
    def test_no_transactions_returns_none(self, user):
        assert user.experience is None

    def test_single_transaction(self, user):
        ExperienceTransaction.objects.create(user=user, amount=100)
        assert user.experience == 100

    def test_multiple_transactions_summed(self, user):
        ExperienceTransaction.objects.create(user=user, amount=100)
        ExperienceTransaction.objects.create(user=user, amount=250)
        assert user.experience == 350

    def test_zero_amount_transaction(self, user):
        ExperienceTransaction.objects.create(user=user, amount=0)
        assert user.experience == 0

    def test_only_counts_own_transactions(self, user, db):
        other = User.objects.create_user(email="other@example.com", password="pass")
        ExperienceTransaction.objects.create(user=other, amount=500)
        assert user.experience is None