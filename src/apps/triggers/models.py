from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from src.utils.celery import plan_task
from src.utils.db import TimestampModelMixin


class Trigger(TimestampModelMixin, models.Model):
    name = models.CharField(
        max_length=250,
        verbose_name=_("name"),
        help_text=_("Name of the trigger."),
        null=False,
        blank=False,
    )
    description = models.TextField(
        verbose_name=_("description"),
        help_text=_("Description of the trigger."),
        null=True,
        blank=True,
    )
    is_triggered = models.BooleanField(
        default=False,
        null=False,
        blank=False,
        verbose_name=_("is triggered"),
        help_text=_("Is the trigger triggered."),
    )
    triggered_at = models.DateTimeField(
        default=timezone.now,
        null=False,
        blank=False,
        verbose_name=_("triggered at"),
        help_text=_("Date and time of the trigger."),
    )

    def save(
            self,
            *args,
            **kwargs,
    ):
        super().save(*args, **kwargs)
        plan_task(
            "src.apps.triggers.tasks.trigger",
            args=(self.id,),
            time=self.triggered_at,
            name=f"Trigger {self.id}",
            remove_existing=True,
        )

    def __str__(self):
        return f"{self.name} - {self.triggered_at}"
