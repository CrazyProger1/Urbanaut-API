import src.apps.accounts.i18n
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.admin import GroupAdmin as BaseGroupAdmin
from django.contrib.auth.models import Group
from django.utils.translation import gettext_lazy as _

from unfold.forms import AdminPasswordChangeForm, UserChangeForm, UserCreationForm
from unfold.admin import ModelAdmin, StackedInline

from src.apps.accounts.models import User, Settings, Username
from src.apps.accounts.sites import site
from src.apps.accounts.admin.achivements import AchievementAdmin, AchievementInline
from src.apps.accounts.admin.referrals import (
    ReferralInline,
    ReferralCodeAdmin,
    ReferralAdmin,
    ReferralCodeInline,
)

admin.site.unregister(Group)


@admin.register(Settings)
class SettingsAdmin(ModelAdmin):
    autocomplete_fields = ("country",)


@admin.register(Username)
class UsernameAdmin(ModelAdmin):
    pass


class SettingsInline(StackedInline):
    model = Settings
    extra = 0
    can_delete = False
    tab = True
    verbose_name = _("Settings")
    verbose_name_plural = _("Settings")
    autocomplete_fields = ("country",)

    def has_add_permission(self, request, obj):
        return False


class UsernameInline(StackedInline):
    model = Username
    extra = 0
    tab = True
    verbose_name = _("Username")
    verbose_name_plural = _("Usernames")


@admin.register(User, site=site)
class UserAdmin(BaseUserAdmin, ModelAdmin):
    form = UserChangeForm
    add_form = UserCreationForm
    change_password_form = AdminPasswordChangeForm
    inlines = (
        SettingsInline,
        UsernameInline,
        AchievementInline,
        ReferralCodeInline,
    )
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        (_("Personal info"), {"fields": ("first_name", "last_name", "bio", "born_at",)}),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "created_at")}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("email", "usable_password", "password1", "password2"),
            },
        ),
    )
    list_display = ("email", "first_name", "last_name", "is_staff", "created_at")
    list_filter = ("is_staff", "is_superuser", "is_active", "groups")
    search_fields = ("first_name", "last_name", "email")
    ordering = ("created_at",)
    readonly_fields = ("created_at",)


@admin.register(Group, site=site)
class GroupAdmin(BaseGroupAdmin, ModelAdmin):
    pass
