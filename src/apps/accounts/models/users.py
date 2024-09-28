from django.contrib.auth.validators import UnicodeUsernameValidator
from django.db import models
from django.contrib.auth.models import PermissionsMixin, AbstractBaseUser
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from src.apps.accounts.enums import UserRank
from src.apps.accounts.managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    username_validator = UnicodeUsernameValidator()

    id = models.BigIntegerField(
        primary_key=True,
        verbose_name=_("Telegram ID"),
        help_text=_("Telegram User ID"),
    )

    username = models.CharField(
        max_length=150,
        blank=True,
        null=True,
        validators=[username_validator],
        verbose_name=_("Username"),
        help_text=_(""),
    )
    nickname = models.CharField(
        max_length=150,
        blank=True,
        null=True,
        verbose_name=_("Nickname"),
        help_text=_("Nickname of the user."),
    )
    first_name = models.CharField(
        max_length=150,
        blank=True,
        verbose_name=_("First Name"),
        help_text=_(""),
    )
    last_name = models.CharField(
        max_length=150,
        blank=True,
        verbose_name=_("Last Name"),
        help_text=_(""),
    )
    email = models.EmailField(
        blank=True,
        verbose_name=_("Email Address"),
        help_text=_(""),
    )
    is_staff = models.BooleanField(
        default=False,
        verbose_name=_("Staff Status"),
        help_text=_("Designates whether the user can log into this admin site."),
    )
    is_active = models.BooleanField(
        default=True,
        verbose_name=_("Active"),
        help_text=_(
            "Designates whether this user should be treated as active. "
            "Unselect this instead of deleting accounts."
        ),
    )
    joined_at = models.DateTimeField(
        default=timezone.now,
        verbose_name=_("Joined At"),
        help_text=_(""),
    )
    born_at = models.DateField(
        default=None,
        null=True,
        blank=True,
        verbose_name=_("Birth Date"),
        help_text=_(""),
    )
    rank = models.CharField(
        choices=UserRank,
        default=UserRank.NEWBIE,
        blank=False,
        null=False,
        verbose_name=_("Rank"),
        help_text=_("The rank of the user."),
    )
    experience = models.PositiveIntegerField(
        default=0,
        blank=False,
        null=False,
        verbose_name=_("Experience"),
        help_text=_("The experience of the user."),
    )
    karma = models.IntegerField(
        default=0,
        blank=False,
        null=False,
        verbose_name=_("Karma"),
        help_text=_("The karma of the user."),
    )
    avatar = models.ForeignKey(
        "media.File",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name=_("Avatar"),
        help_text=_("The avatar of the user."),
    )

    EMAIL_FIELD = "email"
    USERNAME_FIELD = "id"

    objects = UserManager()

    class Meta:
        verbose_name = _("User")
        verbose_name_plural = _("Users")

    def __str__(self):
        return f"{type(self).__name__}(id={self.id})"
