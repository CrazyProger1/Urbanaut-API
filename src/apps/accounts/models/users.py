from django.contrib.auth.validators import UnicodeUsernameValidator
from django.db import models
from django.contrib.auth.models import PermissionsMixin, AbstractBaseUser
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from src.apps.accounts.managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    username_validator = UnicodeUsernameValidator()

    id = models.BigIntegerField(
        _("Telegram ID"),
        primary_key=True,
        help_text=_("Telegram User ID"),
    )

    username = models.CharField(
        _("Username"),
        max_length=150,
        blank=True,
        null=True,
        validators=[username_validator],
    )
    first_name = models.CharField(_("First Name"), max_length=150, blank=True)
    last_name = models.CharField(_("Last Name"), max_length=150, blank=True)
    email = models.EmailField(_("Email Address"), blank=True)
    is_staff = models.BooleanField(
        _("Staff Status"),
        default=False,
        help_text=_("Designates whether the user can log into this admin site."),
    )
    is_active = models.BooleanField(
        _("Active"),
        default=True,
        help_text=_(
            "Designates whether this user should be treated as active. "
            "Unselect this instead of deleting accounts."
        ),
    )
    joined_at = models.DateTimeField(_("Joined At"), default=timezone.now)

    EMAIL_FIELD = "email"
    USERNAME_FIELD = "id"

    objects = UserManager()

    class Meta:
        verbose_name = _("User")
        verbose_name_plural = _("Users")

    def __str__(self):
        return f"{type(self).__name__}(id={self.id})"
