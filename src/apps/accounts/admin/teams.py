from unfold.admin import ModelAdmin
from django.contrib import admin
from modeltranslation.admin import TabbedTranslationAdmin

from src.apps.accounts.models import Team, TeamMember


@admin.register(Team)
class TeamAdmin(ModelAdmin, TabbedTranslationAdmin):
    pass


@admin.register(TeamMember)
class TeamMemberAdmin(ModelAdmin, TabbedTranslationAdmin):
    pass
