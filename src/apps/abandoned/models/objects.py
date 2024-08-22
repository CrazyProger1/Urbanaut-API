from django.contrib.auth import get_user_model
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext as _

from src.apps.abandoned.models.constants import OBJECT_NAME_MAX_LENGTH, SECURITY_LEVEL_LENGTH, \
    OBJECT_PRESERVATION_LEVEL_LENGTH, OBJECT_DIFFICULTY_LEVEL_LENGTH
from src.apps.abandoned.models.enums import SecurityLevel, PreservationLevel, DifficultyLevel

User = get_user_model()


class AbandonedObject(models.Model):
    class Meta:
        verbose_name = _("Object")
        verbose_name_plural = _("Objects")

    area = models.ForeignKey(
        "AbandonedArea",
        on_delete=models.CASCADE,
        related_name="objects",
        null=True,
        blank=True,
        verbose_name=_("Area"),
        help_text=_("Area that contains current object."),
    )
    name = models.CharField(
        max_length=OBJECT_NAME_MAX_LENGTH,
        verbose_name=_("Name"),
        help_text=_("Name of the abandoned object."),
        null=False,
        blank=False,
    )
    description = models.TextField(
        verbose_name=_("Description"),
        help_text=_("Description of the abandoned object."),
        null=True,
        blank=True,
    )
    hidden = models.BooleanField(
        verbose_name=_("Hidden"),
        help_text=_("Hidden from general users and available only for admins."),
        default=False,
        null=False,
        blank=False,
    )
    security_level = models.CharField(
        max_length=SECURITY_LEVEL_LENGTH,
        choices=SecurityLevel,
        default=SecurityLevel.NONE,
        null=False,
        blank=False,
        verbose_name=_("Security Level"),
        help_text=_("Security level of the object."),
    )
    preservation_level = models.CharField(
        max_length=OBJECT_PRESERVATION_LEVEL_LENGTH,
        choices=PreservationLevel,
        default=PreservationLevel.HIGH,
        null=False,
        blank=False,
        verbose_name=_("Preservation Level"),
        help_text=_("Preservation level of the object."),
    )
    difficulty_level = models.CharField(
        max_length=OBJECT_DIFFICULTY_LEVEL_LENGTH,
        choices=DifficultyLevel,
        default=DifficultyLevel.NEWBIE,
        null=False,
        blank=False,
        verbose_name=_("Difficulty Level"),
        help_text=_("Difficulty level of the object."),
    )
    created_at = models.DateTimeField(
        verbose_name=_("Created At"),
        help_text=_("Object creation date and time."),
        default=timezone.now,
    )
    updated_at = models.DateTimeField(
        verbose_name=_("Updated At"),
        help_text=_("Object updated date and time."),
        auto_now=True,
    )
    built_at = models.DateField(
        verbose_name=_("Built At"),
        help_text=_("Object built date and time."),
        null=True,
        blank=True,
    )
    abandoned_at = models.DateField(
        verbose_name=_("Abandoned At"),
        help_text=_("When object became abandoned date and time."),
        null=True,
        blank=True,
    )
    creator = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        related_name="objects",
        blank=True,
        null=True,
        verbose_name=_("Creator"),
        help_text=_(""),
    )

    def __str__(self):
        return f"Object(name={self.name})"
