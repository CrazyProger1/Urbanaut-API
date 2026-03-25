from django.conf import settings
from django.db import models
from django.utils import timezone

from src.utils.django.db import CreatedAtMixin


class UserViews(CreatedAtMixin, models.Model):
    user = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    views = models.ForeignKey(
        to="Views",
        on_delete=models.CASCADE,
    )


class Views(models.Model):
    views = models.ManyToManyField(
        to=settings.AUTH_USER_MODEL,
        through=UserViews,
        blank=True,
    )

    def count(self):
        return self.views.count()

    def increase(self, user):
        if not UserViews.objects.filter(
                user=user,
                created_at__gte=timezone.now() - settings.USER_VIEW_EXPIRATION_SECONDS,
        ).exists():
            UserViews.objects.create(user=user, views=self)


class ViewsMixin(models.Model):
    views = models.OneToOneField(
        to=Views,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )

    def save(
            self,
            *args,
            **kwargs,
    ):
        if not self.views_id:
            self.views = Views.objects.create()

        super().save(*args, **kwargs)

    class Meta:
        abstract = True
