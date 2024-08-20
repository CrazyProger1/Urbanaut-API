from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

from src.apps.accounts.models import Team


@admin.register(Team)
class TeamAdmin(TranslationAdmin):
    pass
