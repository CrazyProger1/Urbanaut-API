from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from modeltranslation.admin import TabbedTranslationAdmin
from unfold.admin import ModelAdmin, StackedInline

from src.apps.accounts.models import Team, TeamMember
from src.apps.accounts.sites import site


class TeamMemberInline(StackedInline):
    model = TeamMember
    extra = 1
    tab = True
    verbose_name = _("Member")
    verbose_name_plural = _("Members")
    autocomplete_fields = (
        "member",
        "team",
    )


@admin.register(Team, site=site)
class TeamAdmin(ModelAdmin, TabbedTranslationAdmin):
    inlines = (TeamMemberInline,)
    list_display = ("name",)
    search_fields = ("name",)
    autocomplete_fields = (
        "created_by",
    )
