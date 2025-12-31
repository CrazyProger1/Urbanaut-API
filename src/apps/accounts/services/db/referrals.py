from datetime import timedelta

from django.utils import timezone

from src.apps.accounts.models import ReferralCode, Referral


def get_all_referral_codes():
    return ReferralCode.objects.all()


def get_user_referral_codes(user):
    return user.referral_codes.all()


def get_referral_code_or_none(**data):
    return ReferralCode.objects.filter(**data).first()


def apply_referral_code(code: ReferralCode, user) -> Referral:
    return Referral.objects.create(code=code, user=user)
