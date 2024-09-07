from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

from src.apps.abandoned.models import Participation


@admin.register(Participation)
class ParticipationAdmin(TranslationAdmin):
    list_display = ("event",)
