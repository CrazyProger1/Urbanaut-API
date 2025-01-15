from unfold.admin import ModelAdmin
from django.contrib import admin

from src.apps.dashboard.admin import site
from src.apps.media.forms import FileForm
from src.apps.media.models import File


@admin.register(File, site=site)
class FileAdmin(ModelAdmin):
    list_display = ("id", "creator", "type")
    list_display_links = ("creator",)
    form = FileForm
