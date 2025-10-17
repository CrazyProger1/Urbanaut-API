from django.contrib.auth.validators import UnicodeUsernameValidator
from django.db import models
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _

from src.apps.accounts.models import User
from src.utils.django.db import CreatedAtMixin


class Username(CreatedAtMixin, models.Model):
    owned_by = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="usernames",
    )
    username = models.SlugField(
        max_length=150,
        unique=True,
        db_index=True,
        validators=(UnicodeUsernameValidator(),),
        verbose_name=_("username"),
        help_text=_("Unique user username."),
    )

    def __str__(self):
        return self.username
