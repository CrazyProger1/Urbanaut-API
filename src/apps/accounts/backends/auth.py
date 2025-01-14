import hashlib
import hmac
import json
import logging
from datetime import datetime, timezone
from operator import itemgetter
from urllib.parse import unquote, parse_qsl

from django.conf import settings

from rest_framework import authentication, exceptions

from src.apps.accounts.services.db import get_user_or_create

logger = logging.getLogger(__name__)


class TMAAuthentication(authentication.BaseAuthentication):

    def parse_data(self, header: bytes) -> dict | None:
        if not header:
            return None

        header = header.decode("utf-8")

        try:
            header = unquote(header)
            parsed_data = dict(parse_qsl(header))
        except ValueError:
            return None

        return parsed_data

    def has_keys(self, parsed_data) -> bool:
        return "hash" in parsed_data or "auth_date" in parsed_data

    def validate_auth_date(self, parsed_data: dict):
        auth_date = datetime.fromtimestamp(
            int(parsed_data["auth_date"]), tz=timezone.utc
        )
        current_time = datetime.now(timezone.utc)
        time_difference = current_time - auth_date

        if time_difference > settings.AUTHENTICATION_TMA_INITDATA_LIFETIME:
            raise exceptions.AuthenticationFailed("Authentication data is expired")

    def validate_hash(self, parsed_data: dict):
        data_hash = parsed_data.pop("hash")
        data_check_string = "\n".join(
            f"{key}={value}"
            for key, value in sorted(parsed_data.items(), key=itemgetter(0))
        )
        secret_key = hmac.new(
            key=b"WebAppData",
            msg=settings.TELEGRAM_BOT_TOKEN.encode(),
            digestmod=hashlib.sha256,
        )
        calculated_hash = hmac.new(
            key=secret_key.digest(),
            msg=data_check_string.encode(),
            digestmod=hashlib.sha256,
        ).hexdigest()

        if calculated_hash != data_hash:
            raise exceptions.AuthenticationFailed("Hash mismatch")

    def update_user(self, user, data: dict):
        user.username = data.get("username", user.username)
        user.first_name = data.get("first_name", user.first_name)
        user.last_name = data.get("last_name", user.last_name)
        user.save()

    def get_user(self, parsed_data: dict):
        try:
            user_data = json.loads(parsed_data.get("user", "{}"))
        except json.JSONDecodeError:
            raise ValueError("Invalid JSON in 'user' field")

        pk = user_data.get("id")

        user = get_user_or_create(
            id=pk,
        )
        self.update_user(
            user=user,
            data=user_data,
        )

        return user

    def authenticate(self, request):
        header = authentication.get_authorization_header(request)

        logger.info("Authenticating user...")

        if not header:
            return None

        logger.debug(f"Authentication header obtained")

        parsed_data = self.parse_data(header=header)

        logger.debug(f"Data parsed")

        self.validate_auth_date(parsed_data=parsed_data)

        logger.debug("Auth data validated")

        self.validate_hash(parsed_data=parsed_data)

        logger.debug("Hash validated")

        user = self.get_user(parsed_data=parsed_data)

        logger.info(f"User authenticated: {user}")

        return user, header
