from django.contrib import admin
from unfold.admin import ModelAdmin

from src.apps.accounts.sites import site
from src.apps.finances.models import Balance


@admin.register(Balance, site=site)
class BalanceAdmin(ModelAdmin):
    list_display = ("id", "owned_by", "is_pool", "created_at")
