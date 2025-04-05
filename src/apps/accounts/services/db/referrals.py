from django.db import models

from src.apps.accounts.models import ReferralLink, ReferralLinkUsage
from src.utils.db import get_all_objects, filter_objects, get_object_or_none


def get_all_referral_links() -> models.QuerySet[ReferralLink]:
    return get_all_objects(source=ReferralLink)


def get_user_referral_links(user) -> models.QuerySet[ReferralLink]:
    return filter_objects(source=ReferralLink, referrer=user)


def get_non_user_referral_links(user) -> models.QuerySet[ReferralLink]:
    return get_all_referral_links().exclude(referrer=user)


def apply_referral_link(user, link: ReferralLink) -> bool:
    applied_link = get_object_or_none(source=ReferralLinkUsage, referral=user)
    if applied_link:
        return False

    link.referrals.add(user)
    return True
