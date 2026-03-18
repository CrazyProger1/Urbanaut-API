from django.contrib import admin
from unfold.admin import ModelAdmin, StackedInline
from django.utils.translation import gettext_lazy as _

from src.apps.accounts.sites import site
from src.apps.expeditions.models import Participation


class ParticipationInline(StackedInline):
    model = Participation
    extra = 1
    tab = True
    verbose_name = _("Participation")
    verbose_name_plural = _("Participations")
    autocomplete_fields = ("participant",)


@admin.register(Participation, site=site)
class ParticipationAdmin(ModelAdmin):
    pass
