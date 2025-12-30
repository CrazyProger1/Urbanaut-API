import uuid

from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _

from src.utils.django.db import CreatedAtMixin


class Referral(CreatedAtMixin, models.Model):
    class Meta:
        verbose_name = _("Referral")
        verbose_name_plural = _("Referrals")

    code = models.ForeignKey(
        to="ReferralCode",
        on_delete=models.CASCADE,
        related_name="referrals",
        null=False,
        blank=False,
    )
    user = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="referral",
        unique=True,
        null=False,
        blank=False,
    )

    def __str__(self):
        return f"{self.user} referred by {self.code}"


class ReferralCode(CreatedAtMixin, models.Model):
    class Meta:
        verbose_name = _("Referral Code")
        verbose_name_plural = _("Referral Codes")

    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        null=False,
        blank=False,
        related_name="referral_codes",
        verbose_name=_("created by"),
    )
    code = models.SlugField(
        max_length=150,
        unique=True,
        null=False,
        blank=False,
        default=uuid.uuid4,
        verbose_name=_("code"),
    )
    referred_users = models.ManyToManyField(
        to=settings.AUTH_USER_MODEL,
        through=Referral,
        related_name="referred_by_code",
    )

    def __str__(self):
        return self.code
