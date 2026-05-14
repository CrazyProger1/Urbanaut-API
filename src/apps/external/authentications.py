import logging

from django.utils import timezone
from rest_framework import authentication, exceptions

from src.apps.external.models import Key
from src.apps.external.services.db import get_key_or_none
from src.utils.django.hmac import verify_signature

logger = logging.getLogger(__name__)


class HMACAuthentication(authentication.BaseAuthentication):

    def _get_signature(self, request) -> str:
        return request.META.get("HTTP_X_API_SIGNATURE")

    def _get_key_id(self, request) -> str:
        return request.META.get("HTTP_X_API_KEY")

    def _get_key(self, pk: str) -> Key:
        key = get_key_or_none(pk=pk)

        if not key:
            logger.warning("HMAC authentication failed: key %s not found", pk)
            raise exceptions.AuthenticationFailed("Key not found")

        return key

    def _verify_key(self, key: Key):
        if key.expired_at and key.expired_at < timezone.now():
            logger.warning("HMAC authentication failed: key %s expired at %s", key.pk, key.expired_at)
            raise exceptions.AuthenticationFailed("Key expired")

        if key.is_revoked:
            logger.warning("HMAC authentication failed: key %s is revoked", key.pk)
            raise exceptions.AuthenticationFailed("Key is revoked")

    def _verify_request(self, request, key: Key, signature: str):
        try:
            signature_bytes = bytes.fromhex(signature)
        except ValueError:
            logger.warning("HMAC authentication failed: signature is not valid hex")
            raise exceptions.AuthenticationFailed("Request lost integrity")

        if not verify_signature(
                key=key.key,
                method=request.method,
                signature=signature_bytes,
                url=request.build_absolute_uri(),
                payload=request.body,
        ):
            logger.warning(
                "HMAC authentication failed: invalid signature for key %s on %s %s",
                key.pk,
                request.method,
                request.build_absolute_uri(),
            )
            raise exceptions.AuthenticationFailed("Request lost integrity")

    def authenticate(self, request):
        key_id = self._get_key_id(request=request)
        signature = self._get_signature(request=request)

        if not key_id or not signature:
            return None

        logger.debug(
            "Authenticating %s %s using HMAC with key %s",
            request.method,
            request.build_absolute_uri(),
            key_id,
        )

        key = self._get_key(pk=key_id)

        self._verify_key(key=key)
        self._verify_request(request=request, key=key, signature=signature)

        logger.info(
            "HMAC authentication succeeded: user=%s key=%s",
            key.created_by_id,
            key.pk,
        )

        return key.created_by, key
