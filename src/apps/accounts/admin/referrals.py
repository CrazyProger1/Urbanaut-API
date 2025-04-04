from unfold.admin import ModelAdmin, TabularInline
from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from src.apps.accounts.models import ReferralLink, ReferralLinkUsage
from src.apps.dashboard.admin.site import site


class ReferralLinkUsageInline(TabularInline):
    model = ReferralLinkUsage
    extra = 0
    verbose_name = _("Usage")
    verbose_name_plural = _("Usages")
    tab = True
    show_change_link = True


@admin.register(ReferralLink, site=site)
class ReferralLinkAdmin(ModelAdmin):
    list_display = (
        "id",
        "referrer",
    )
    list_display_links = (
        "referrer",
    )
    inlines = (
        ReferralLinkUsageInline,
    )
