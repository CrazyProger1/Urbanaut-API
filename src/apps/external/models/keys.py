import secrets
import uuid

from cryptography.fernet import Fernet
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.conf import settings

from src.utils.django.db import TimestampMixin


class Key(TimestampMixin, models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )
    application = models.ForeignKey(
        to="Application",
        on_delete=models.CASCADE,
        verbose_name=_("application"),
        help_text=_("Application the key belongs to."),
        related_name="keys",
        null=False,
        blank=False,
    )
    created_by = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="keys",
    )
    name = models.CharField(
        verbose_name=_("name"),
        max_length=255,
        null=False,
        blank=False,
    )
    is_revoked = models.BooleanField(
        default=False,
        verbose_name=_("is revoked"),
        help_text=_("Whether the key is revoked."),
        blank=False,
        null=False,
    )
    encrypted_key = models.BinaryField(
        verbose_name=_("encrypted key"),
        null=False,
        blank=False,
        help_text=_("Encrypted key."),
    )
    expired_at = models.DateTimeField(
        verbose_name=_("expired at"),
        null=True,
        blank=True,
    )

    def _issue(self):
        key = secrets.token_bytes(32)
        self.encrypted_key = Fernet(settings.HMAC_MASTER_KEY).encrypt(key)

    @property
    def key(self) -> bytes:
        return Fernet(settings.HMAC_MASTER_KEY).decrypt(bytes(self.encrypted_key))

    def save(
        self,
        *args,
        **kwargs,
    ):
        if not self.encrypted_key:
            self._issue()

        super().save(*args, **kwargs)

    class Meta:
        verbose_name = _("Key")
        verbose_name_plural = _("Keys")

    def __str__(self):
        return self.name
