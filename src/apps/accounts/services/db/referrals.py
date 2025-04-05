from django.db import models

from src.apps.accounts.models import ReferralLink
from src.utils.db import get_all_objects, filter_objects


def get_all_referral_links() -> models.QuerySet[ReferralLink]:
    return get_all_objects(source=ReferralLink)


def get_user_referral_links(user) -> models.QuerySet[ReferralLink]:
    return filter_objects(source=ReferralLink, referrer=user)


def get_non_user_referral_links(user) -> models.QuerySet[ReferralLink]:
    return get_all_referral_links().exclude(referrer=user)
