from django.db import models
from django.utils.translation import gettext_lazy as _
from src.apps.actions.enums import ActionType

ActionType.register("REGISTERED", "REGISTERED", _("REGISTERED"))
ActionType.register("LOGGED_IN", "LOGGED IN", _("LOGGED IN"))
ActionType.register("LOGGED_OUT", "LOGGED OUT", _("LOGGED OUT"))


class UITheme(models.TextChoices):
    LIGHT = "LIGHT", _("LIGHT")
    DARK = "DARK", _("DARK")
