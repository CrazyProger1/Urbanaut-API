from unfold.admin import ModelAdmin
from django.contrib import admin

from src.apps.media.forms import FileForm

from src.apps.accounts.sites import site
from src.apps.media.models import File


@admin.register(File, site=site)
class FileAdmin(ModelAdmin):
    list_display = ("id", "created_by", "type")
    list_display_links = ("created_by",)
    form = FileForm
