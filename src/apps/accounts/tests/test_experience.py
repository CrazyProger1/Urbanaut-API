import pytest

from src.apps.accounts.models import User, ExperienceTransaction
from src.apps.accounts.services.db.experience import make_experience_transaction


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


@pytest.mark.django_db
class TestMakeExperienceTransaction:
    def test_creates_transaction(self, user):
        tx = make_experience_transaction(user=user, amount=100)
        assert tx.pk is not None
        assert tx.user == user
        assert tx.amount == 100

    def test_zero_raises(self, user):
        with pytest.raises(ValueError):
            make_experience_transaction(user=user, amount=0)

    def test_negative_raises(self, user):
        with pytest.raises(ValueError):
            make_experience_transaction(user=user, amount=-1)

    def test_persisted_to_db(self, user):
        make_experience_transaction(user=user, amount=50)
        assert ExperienceTransaction.objects.filter(user=user).count() == 1

    def test_float_amount_cast_to_int(self, user):
        tx = make_experience_transaction(user=user, amount=9.9)
        assert tx.amount == 9