from unfold.admin import ModelAdmin
from django.contrib import admin
from modeltranslation.admin import TabbedTranslationAdmin

from src.apps.abandoned.models import Participation
from src.apps.dashboard.admin.site import site


@admin.register(Participation, site=site)
class ParticipationAdmin(ModelAdmin, TabbedTranslationAdmin):
    list_display = ("event",)
