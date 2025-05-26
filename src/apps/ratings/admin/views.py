from unfold.admin import TabularInline
from django.utils.translation import gettext_lazy as _

from src.apps.ratings.models import View


class ViewInline(TabularInline):
    model = View
    tab = True
    extra = 0
    show_change_link = True
    verbose_name = _("View")
    verbose_name_plural = _("Views")
