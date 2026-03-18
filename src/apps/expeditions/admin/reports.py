from django.contrib import admin
from unfold.admin import ModelAdmin, StackedInline
from django.utils.translation import gettext_lazy as _

from src.apps.accounts.sites import site
from src.apps.expeditions.models import Report


class ReportInline(StackedInline):
    model = Report
    extra = 1
    tab = True
    verbose_name = _("Report")
    verbose_name_plural = _("Reports")


@admin.register(Report, site=site)
class ReportAdmin(ModelAdmin):
    pass
