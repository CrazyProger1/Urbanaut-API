from django.db import models

from django.utils.translation import gettext_lazy as _
from src.utils.db import TimestampModelMixin


class NotificationEvent(models.Model):
    event = models.ForeignKey(
        "Event",
        on_delete=models.CASCADE,
        blank=False,
        null=False,
        verbose_name=_("event"),
    )
    notification = models.ForeignKey(
        "Notification",
        on_delete=models.CASCADE,
        blank=False,
        null=False,
        verbose_name=_("notification"),
    )


class NewsletterEvent(models.Model):
    event = models.ForeignKey(
        "Event",
        on_delete=models.CASCADE,
        blank=False,
        null=False,
        verbose_name=_("event"),
    )
    newsletter = models.ForeignKey(
        "Newsletter",
        on_delete=models.CASCADE,
        blank=False,
        null=False,
        verbose_name=_("newsletter"),
    )


class CategoryEvent(models.Model):
    event = models.ForeignKey(
        "Event",
        on_delete=models.CASCADE,
        blank=False,
        null=False,
        verbose_name=_("event"),
    )
    category = models.ForeignKey(
        "Category",
        on_delete=models.CASCADE,
        blank=False,
        null=False,
        verbose_name=_("category"),
    )


class TriggerEvent(models.Model):
    event = models.ForeignKey(
        "Event",
        on_delete=models.CASCADE,
        blank=False,
        null=False,
        verbose_name=_("event"),
    )
    # trigger = models.ForeignKey(
    #     "triggers.Trigger",
    #     on_delete=models.CASCADE,
    #     blank=False,
    #     null=False,
    #     verbose_name=_("trigger"),
    # )


class Event(TimestampModelMixin, models.Model):
    name = models.CharField(
        max_length=250,
        verbose_name=_("name"),
        help_text=_("Name of the event."),
        null=False,
        blank=False,
    )
    description = models.TextField(
        verbose_name=_("description"),
        help_text=_("Description of the event."),
        null=True,
        blank=True,
    )
    newsletters = models.ManyToManyField(
        "Newsletter",
        through=NewsletterEvent,
        blank=True,
        verbose_name=_("newsletters"),
        help_text=_("Newsletters included to this event.")
    )
    notifications = models.ManyToManyField(
        "Notification",
        through=NotificationEvent,
        blank=True,
        verbose_name=_("notifications"),
        help_text=_("Notifications included to this event.")
    )
    categories = models.ManyToManyField(
        "Category",
        through=CategoryEvent,
        blank=True,
        verbose_name=_("categories"),
        help_text=_("Recipient categories.")
    )
    # triggers = models.ManyToManyField(
    #     "triggers.Trigger",
    #     through=TriggerEvent,
    #     blank=True,
    #     verbose_name=_("triggers"),
    #     help_text=_("Triggers included to this event.")
    # )

    def __str__(self):
        return self.name
