from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _

from src.utils.db import TimestampModelMixin, CreatedAtModelMixin


class ReferralLinkUsage(CreatedAtModelMixin, models.Model):
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

    def __str__(self):
        return str(self.referral)


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

    @property
    def link(self):
        # TODO: Make this configurable
        return f"https://t.me/urbanautbot?start={self.code}"

    def __str__(self):
        return self.link
