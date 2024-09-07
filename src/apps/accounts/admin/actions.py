from django.contrib import admin


from src.apps.accounts.models import UserAction


@admin.register(UserAction)
class UserActionAdmin(admin.ModelAdmin):
    list_display = ("id", "type", "user")
    search_fields = ("type",)
    list_filter = ("type",)
    list_display_links = ("type",)
