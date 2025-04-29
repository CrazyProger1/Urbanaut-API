from django.contrib.auth import get_user_model
from django.db import models

from django.utils.translation import gettext_lazy as _
from mdeditor.fields import MDTextField

from src.apps.abandoned.enums import (
    SecurityLevel,
    PreservationLevel,
    DifficultyLevel,
)
from src.apps.media.enums import FileType
from src.apps.permissions.models import PermissionBaseModel
from src.apps.ratings.models import RatingMixin
from src.utils.db.models import TimestampModelMixin

User = get_user_model()


class AbandonedObjectCategory(models.Model):
    object = models.ForeignKey(
        "AbandonedObject",
        on_delete=models.CASCADE,
    )

    category = models.ForeignKey(
        "abandoned.Category",
        on_delete=models.CASCADE,
    )


class AbandonedObjectFile(models.Model):
    class Meta:
        verbose_name = _("file")
        verbose_name_plural = _("files")

    file = models.ForeignKey(
        "media.File",
        on_delete=models.CASCADE,
    )
    object = models.ForeignKey(
        "AbandonedObject",
        on_delete=models.CASCADE,
    )
    priority = models.IntegerField(
        default=0,
    )


class AbandonedObject(TimestampModelMixin, RatingMixin, PermissionBaseModel):
    class Meta:
        verbose_name = _("object")
        verbose_name_plural = _("objects")

    categories = models.ManyToManyField(
        to="abandoned.Category",
        through=AbandonedObjectCategory,
        verbose_name=_("categories"),
        help_text=_("Categories related to current object."),
    )
    area = models.ForeignKey(
        "AbandonedArea",
        on_delete=models.CASCADE,
        related_name="abandoned_objects",
        null=True,
        blank=True,
        verbose_name=_("area"),
        help_text=_("Area that contains current object."),
    )
    name = models.CharField(
        max_length=250,
        verbose_name=_("name"),
        help_text=_("Name of the abandoned object."),
        null=False,
        blank=False,
    )
    short_description = models.CharField(
        verbose_name=_("short description"),
        help_text=_("Short description of the abandoned object for the objects page.")
    )
    description = MDTextField(
        verbose_name=_("description"),
        help_text=_("Description of the abandoned object."),
        null=True,
        blank=True,
    )
    security_level = models.CharField(
        choices=SecurityLevel,
        default=SecurityLevel.NO,
        null=False,
        blank=False,
        verbose_name=_("security Level"),
        help_text=_("Security level of the object."),
    )
    preservation_level = models.CharField(
        choices=PreservationLevel,
        default=PreservationLevel.HIGH,
        null=False,
        blank=False,
        verbose_name=_("preservation Level"),
        help_text=_("Preservation level of the object."),
    )
    difficulty_level = models.CharField(
        choices=DifficultyLevel,
        default=DifficultyLevel.NEWBIE,
        null=False,
        blank=False,
        verbose_name=_("difficulty level"),
        help_text=_("Difficulty level of the object."),
    )
    built_at = models.DateField(
        verbose_name=_("built at"),
        help_text=_("Object built date and time."),
        null=True,
        blank=True,
    )
    abandoned_at = models.DateField(
        verbose_name=_("abandoned at"),
        help_text=_("When object became abandoned date and time."),
        null=True,
        blank=True,
    )
    created_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        related_name="abandoned_objects",
        blank=True,
        null=True,
        verbose_name=_("created by"),
        help_text=_(""),
    )
    location = models.ForeignKey(
        "geo.Location",
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name="objects",
        verbose_name=_("location"),
        help_text=_("Location of the object."),
    )
    files = models.ManyToManyField(
        "media.File",
        through=AbandonedObjectFile,
        verbose_name=_("files"),
        related_name="abandoned_objects",
        help_text=_("The media files representing this object."),
    )

    def photos(self):
        return self.files.filter(
            type__in=(FileType.PHOTO, FileType.VIDEO)
        ).order_by("type")

    def photo(self):
        photo = self.files.filter(type=FileType.PHOTO).first()
        if photo:
            return photo.src

    def __str__(self):
        return f"Object(name={self.name})"
