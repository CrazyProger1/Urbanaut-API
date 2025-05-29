from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _


class View(models.Model):
    viewed_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    viewed_at = models.DateTimeField(
        auto_now_add=True,
    )
    viewable = models.ForeignKey(
        "Viewable",
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return f"User №{self.viewed_by_id} view"


class Viewable(models.Model):
    viewed_by = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        through=View,
    )
    views = models.PositiveBigIntegerField(
        default=0,
    )

    def __str__(self):
        return str(self.views)


class ViewedByMixin(models.Model):
    viewable = models.OneToOneField(
        Viewable,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name=_("views"),
    )

    def increase_views(self, user):
        if not self.viewable_id:
            self.save()

        View.objects.create(viewed_by=user, viewable=self.viewable)
        self.viewable.views += 1
        self.viewable.save(update_fields=("views",))

    @property
    def views(self) -> int:
        return self.viewable.views

    @property
    def viewed_by(self) -> models.QuerySet:
        return self.viewable.viewed_by.all()

    def save(
            self,
            *args,
            **kwargs,
    ):
        if not self.viewable_id:
            self.viewable = Viewable.objects.create()

        super().save(*args, **kwargs)

    class Meta:
        abstract = True
