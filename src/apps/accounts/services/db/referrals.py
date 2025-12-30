from datetime import timedelta

from django.utils import timezone

from src.apps.accounts.models import ReferralCode, Referral


def _user_is_new(user):
    now = timezone.now()
    return now - user.created_at < timedelta(hours=1)


def _user_is_not_refereed(user):
    return not Referral.objects.filter(user=user).exists()


def _not_same_user(user, code) -> bool:
    return code.created_by != user


def get_all_referral_codes():
    return ReferralCode.objects.all()


def get_user_referral_codes(user):
    return user.referral_codes.all()


def can_apply_referral_code(user, code) -> bool:
    return (
        _user_is_new(user=user)
        and _user_is_not_refereed(user=user)
        and _not_same_user(user=user, code=code)
    )


def apply_referral_code(code: ReferralCode, user) -> Referral:
    return Referral.objects.create(code=code, user=user)
