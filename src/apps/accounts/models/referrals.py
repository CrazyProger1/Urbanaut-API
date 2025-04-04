from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _

from src.utils.db import TimestampModelMixin


class ReferralLinkUsage(TimestampModelMixin, models.Model):
    class Meta:
        verbose_name = _("Referral Link Usage")
        verbose_name_plural = _("Referral Link Usages")
        unique_together = ("link", "referral")

    link = models.ForeignKey(
        to="ReferralLink",
        on_delete=models.CASCADE,
        null=False,
        blank=False,
    )
    referral = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        null=False,
        blank=False,
        unique=True,
    )


class ReferralLink(TimestampModelMixin, models.Model):
    referrer = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        null=False,
        blank=False,
        related_name="referral_links",
        verbose_name=_("Referrer"),
    )
    referrals = models.ManyToManyField(
        to=settings.AUTH_USER_MODEL,
        through=ReferralLinkUsage,
        blank=True,
        verbose_name=_("Referrals"),
    )
    code = models.SlugField(
        unique=True,
        null=False,
        blank=False,
        max_length=50,
        verbose_name=_("Code"),
    )
