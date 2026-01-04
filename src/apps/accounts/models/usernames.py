from django.conf import settings
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.db import models
from django.utils.translation import gettext_lazy as _

from src.utils.django.db import CreatedAtMixin


class Username(CreatedAtMixin, models.Model):
    owned_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
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
    is_initial = models.BooleanField(
        default=False,
        null=False,
        blank=False,
        verbose_name=_("is initial"),
        help_text=_("User's initial username (given when user was created)"),
    )

    def __str__(self):
        return self.username


class UsernameMixin(models.Model):
    class Meta:
        abstract = True

    def _give_initial_username(self):
        from src.apps.accounts.services.db import (
            give_initial_username,
            has_username,
        )

        if not has_username(user=self):
            give_initial_username(user=self)

    def save(
        self,
        *args,
        **kwargs,
    ):
        super().save(*args, **kwargs)
        self._give_initial_username()
