from django.contrib import admin
from unfold.admin import TabularInline, ModelAdmin
from django.utils.translation import gettext_lazy as _

from src.apps.dashboard.admin import site
from src.apps.ratings.models import View, Viewable


class ViewInline(TabularInline):
    model = View
    tab = True
    extra = 0
    show_change_link = True
    verbose_name = _("View")
    verbose_name_plural = _("Views")


@admin.register(Viewable, site=site)
class ViewableAdmin(ModelAdmin):
    inlines = (
        ViewInline,
    )
