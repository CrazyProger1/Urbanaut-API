from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

from src.apps.accounts.models import User


@admin.register(User)
class UserAdmin(TranslationAdmin):
    pass
