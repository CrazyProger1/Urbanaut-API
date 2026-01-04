from src.apps.accounts.models import ReferralCode, Referral, User
from src.apps.accounts.services.db.usernames import get_initial_username


def get_all_referral_codes():
    return ReferralCode.objects.all()


def get_user_referral_codes(user):
    return user.referral_codes.all()


def get_referral_code_or_none(**data):
    return ReferralCode.objects.filter(**data).first()


def apply_referral_code(code: ReferralCode, user) -> Referral:
    return Referral.objects.create(code=code, user=user)


def has_referral_code(user: User) -> bool:
    return user.referral_codes.exists()


def give_referral_code(user: User, code: str) -> ReferralCode:
    return ReferralCode.objects.create(code=code, created_by=user)


def give_initial_referral_code(user: User) -> ReferralCode:
    username = get_initial_username(user=user)
    return give_referral_code(user=user, code=username.username)
