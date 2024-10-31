from unfold.admin import ModelAdmin
from django.contrib import admin
from modeltranslation.admin import TabbedTranslationAdmin

from src.apps.abandoned.models import Participation


@admin.register(Participation)
class ParticipationAdmin(ModelAdmin, TabbedTranslationAdmin):
    list_display = ("event",)
