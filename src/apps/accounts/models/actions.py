from django.db import models
from django.utils.translation import gettext_lazy as _

from src.apps.accounts.enums import UserActionType


class UserAction(models.Model):
    class Meta:
        verbose_name = _("Action")
        verbose_name_plural = _("Actions")

    type = models.CharField(
        choices=UserActionType,
        null=False,
        blank=False,
        verbose_name=_("Type"),
        help_text=_("Type of an action."),
    )
    data = models.JSONField(
        default=dict,
        blank=True,
        null=True,
        verbose_name=_("Data"),
        help_text=_("Action additional data."),
    )
    user = models.ForeignKey(
        "User",
        on_delete=models.CASCADE,
        blank=False,
        null=False,
        verbose_name=_("User"),
        help_text=_("User who made the action."),
    )

    def __str__(self):
        return f"{type(self).__name__}(id={self.id})"
