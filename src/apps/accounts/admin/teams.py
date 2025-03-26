from simple_history.admin import SimpleHistoryAdmin
from unfold.admin import ModelAdmin
from django.contrib import admin
from modeltranslation.admin import TabbedTranslationAdmin

from src.apps.accounts.models import Team, TeamMember
from src.apps.dashboard.admin.site import site


@admin.register(Team, site=site)
class TeamAdmin(ModelAdmin, TabbedTranslationAdmin, SimpleHistoryAdmin):
    pass


@admin.register(TeamMember, site=site)
class TeamMemberAdmin(ModelAdmin, TabbedTranslationAdmin):
    pass
