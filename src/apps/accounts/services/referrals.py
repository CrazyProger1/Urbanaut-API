from django.db import transaction

from src.apps.accounts.models import ReferralCode, Referral
from src.apps.accounts.services.db import create_referral


@transaction.atomic
def apply_referral_code(code: ReferralCode, user) -> Referral:
    from src.apps.accounts.events import UserEventChannel, UserReferralEvent
    referral = create_referral(code=code, user=user)
    UserEventChannel.user_referral.publish(UserReferralEvent(user=user, code=code))
    return referral
