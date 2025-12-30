from django.contrib import admin
from unfold.admin import ModelAdmin, TabularInline
from django.utils.translation import gettext_lazy as _

from src.apps.accounts.models import ReferralCode, Referral
from src.apps.accounts.sites import site


@admin.register(Referral, site=site)
class ReferralAdmin(ModelAdmin):
    list_display = ("code", "created_at")


class ReferralInline(TabularInline):
    tab = True
    model = Referral
    verbose_name = _("Referral")
    verbose_name_plural = _("Referrals")
    extra = 0


@admin.register(ReferralCode, site=site)
class ReferralCodeAdmin(ModelAdmin):
    list_display = ("code", "created_by", "created_at")
    inlines = (ReferralInline,)
