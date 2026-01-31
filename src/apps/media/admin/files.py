from unfold.admin import ModelAdmin
from django.contrib import admin

from src.apps.media.forms import FileForm

from src.apps.accounts.sites import site
from src.apps.media.models import File


@admin.register(File, site=site)
class FileAdmin(ModelAdmin):
    list_display = (
        "id",
        "file_tag",
        "type",
        "created_by",
    )
    list_display_links = (
        "id",
        "file_tag",
    )
    form = FileForm

    def file_tag(self, obj: File):
        return obj.file.name
