from django.db import models
from django.db.models import Subquery

from src.apps.accounts.models import ReferralLink, ReferralLinkUsage, User
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

    if link.referrer == user:
        return False

    link.referrals.add(user)
    return True


def get_user_referrals(user) -> models.QuerySet[User]:
    links = ReferralLink.objects.filter(referrer=user)
    user_ids = (
        ReferralLinkUsage.objects
        .filter(link__in=links)
        .values("referral_id")
    )
    return User.objects.filter(id__in=Subquery(user_ids))


def get_link_referrals(link: ReferralLink) -> models.QuerySet[User]:
    return link.referrals.all()


def get_referral_link_or_none(**data) -> ReferralLink:
    return get_object_or_none(source=ReferralLink, **data)
