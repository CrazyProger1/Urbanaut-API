from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

from src.apps.accounts.models import Team, TeamMember


@admin.register(Team)
class TeamAdmin(TranslationAdmin):
    pass


@admin.register(TeamMember)
class TeamMemberAdmin(TranslationAdmin):
    pass
