from django.contrib import admin

from src.apps.media.models import File


@admin.register(File)
class FileAdmin(admin.ModelAdmin):
    pass
