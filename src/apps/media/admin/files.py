from django.contrib import admin

from src.apps.media.forms import FileForm
from src.apps.media.models import File


@admin.register(File)
class FileAdmin(admin.ModelAdmin):
    list_display = ("id", "creator", "type")
    list_display_links = ("creator",)
    form = FileForm
