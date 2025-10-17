import uuid

from django.db import models
from django.contrib.auth.models import PermissionsMixin, AbstractBaseUser
from django.utils.translation import gettext_lazy as _

from src.apps.accounts.managers import UserManager

from src.utils.django.db import TimestampMixin


class User(TimestampMixin, PermissionsMixin, AbstractBaseUser):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )
    first_name = models.CharField(
        max_length=150,
        blank=True,
        null=True,
        verbose_name=_("first name"),
    )
    last_name = models.CharField(
        max_length=150,
        blank=True,
        null=True,
        verbose_name=_("last name"),
    )
    email = models.EmailField(
        unique=True,
        blank=True,
        null=True,
        verbose_name=_("email address"),
        help_text=_("Email address of the user."),
    )
    is_staff = models.BooleanField(
        default=False,
        verbose_name=_("staff status"),
        help_text=_("Designates whether the user can log into this admin site."),
    )
    is_active = models.BooleanField(
        default=True,
        verbose_name=_("active"),
        help_text=_(
            "designates whether this user should be treated as active. "
            "Unselect this instead of deleting accounts."
        ),
    )
    born_at = models.DateField(
        default=None,
        null=True,
        blank=True,
        verbose_name=_("birth Date"),
        help_text=_("User born at date and time."),
    )

    EMAIL_FIELD = "email"
    USERNAME_FIELD = "email"

    objects = UserManager()

    class Meta:
        verbose_name = _("User")
        verbose_name_plural = _("Users")

    def __str__(self):
        return (
            f"{self.first_name} {self.last_name} ({self.email})"
            if self.first_name or self.last_name
            else self.email
        )
