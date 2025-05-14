from django.db import models

from django.utils.translation import gettext_lazy as _

from src.utils.celery import plan_task
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
        help_text=_("Newsletters included to this event."),
    )
    notifications = models.ManyToManyField(
        "Notification",
        through=NotificationEvent,
        blank=True,
        verbose_name=_("notifications"),
        help_text=_("Notifications included to this event."),
    )
    categories = models.ManyToManyField(
        "Category",
        through=CategoryEvent,
        blank=True,
        verbose_name=_("categories"),
        help_text=_("Recipient categories."),
    )
    triggered_at = models.DateTimeField(
        verbose_name=_("triggered at"),
        help_text=_("Date and time when the event should be/was triggered."),
        null=True,
        blank=True,
    )
    is_active = models.BooleanField(
        default=True,
        verbose_name=_("is active"),
        help_text=_("Is the event active?"),
    )

    def save(
        self,
        *args,
        **kwargs,
    ):
        super().save(*args, **kwargs)
        plan_task(
            time=self.triggered_at,
            task="src.apps.notifier.tasks.events.trigger_event",
            args=(self.id,),
            kwargs={},
            remove_existing=True,
            name=f"Event №{self.id}",
        )

    def __str__(self):
        return self.name
