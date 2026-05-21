from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from unfold.admin import ModelAdmin

from src.apps.accounts.sites import site
from src.apps.external.models import Key
from src.utils.django.admin import CreatedByAdminMixin


@admin.register(Key, site=site)
class KeyAdmin(CreatedByAdminMixin, ModelAdmin):
    created_by_field = "created_by"
    list_display = (
        "name",
        "is_revoked",
        created_by_field,
        "created_at",
        "expired_at",
    )
    autocomplete_fields = (
        created_by_field,
        "application",
    )
    search_fields = ("name",)
    list_filter = ("created_at",)

    readonly_fields = ("key", "id", "created_at", "updated_at")

    fieldsets = (
        (
            _("General"),
            {
                "fields": ("name",),
            },
        ),
        (
            _("Details"),
            {
                "fields": ("is_revoked",),
            },
        ),
        (
            _("Key"),
            {
                "fields": (
                    "key",
                    "id",
                ),
            },
        ),
        (
            _("Meta"),
            {
                "fields": (
                    created_by_field,
                    "created_at",
                    "updated_at",
                ),
            },
        ),
    )

    def key(self, obj: Key):
        return obj.key.hex()

    key.short_description = "Key"
