from django.db import models

from src.apps.accounts.models import ReferralLink
from src.utils.db import get_all_objects


def get_all_referral_links() -> models.QuerySet[ReferralLink]:
    return get_all_objects(source=ReferralLink)


def get_user_referral_links(user) -> models.QuerySet[ReferralLink]:
    return get_all_referral_links().filter(user=user)
