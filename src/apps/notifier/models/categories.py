from django.db import models
from django.utils.translation import gettext_lazy as _
from src.utils.db import TimestampModelMixin


class CategoryRecipient(models.Model):
    user = models.ForeignKey(
        "User",
        on_delete=models.CASCADE,
        blank=False,
        null=False,
        verbose_name=_("user"),
    )
    category = models.ForeignKey(
        "Category",
        on_delete=models.CASCADE,
        blank=False,
        null=False,
        verbose_name=_("category"),
    )


class Category(TimestampModelMixin, models.Model):
    name = models.CharField(
        max_length=250,
        verbose_name=_("name"),
        help_text=_("Name of the category."),
        null=False,
        blank=False,
    )
    description = models.TextField(
        verbose_name=_("description"),
        help_text=_("Description of the category."),
        null=True,
        blank=True,
    )
    recipients = models.ManyToManyField(
        "User",
        through=CategoryRecipient,
        verbose_name=_("recipients"),
        help_text=_("Recipients of the category."),
    )
    is_for_all = models.BooleanField(
        default=False,
        null=False,
        blank=False,
        verbose_name=_("include all"),
        help_text=_("Include all users in the category."),
    )
