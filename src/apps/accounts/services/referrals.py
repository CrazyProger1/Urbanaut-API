from django.db import transaction

from src.apps.accounts.models import ReferralCode, Referral
from src.apps.accounts.services.db import create_referral, is_referral


@transaction.atomic
def try_apply_referral_code(code: ReferralCode, user) -> Referral | None:
    from src.apps.accounts.events import UserEventChannel, UserReferralEvent

    if code.created_by == user:
        # Code creator can't apply code for self
        return None

    if is_referral(user=user, code=code):
        # Code could be applied only once
        return None

    referral = create_referral(code=code, user=user)
    UserEventChannel.user_referral.publish(UserReferralEvent(user=user, code=code))
    return referral
