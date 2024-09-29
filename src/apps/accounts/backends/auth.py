import hashlib
import hmac
import json
from operator import itemgetter
from urllib.parse import parse_qsl

from django.conf import settings

from rest_framework import authentication, exceptions

from src.apps.accounts.services import get_user_or_none


class TMAAuthentication(authentication.BaseAuthentication):

    def authenticate(self, request):
        header = authentication.get_authorization_header(request)

        if not header:
            return None

        header = header.decode("utf-8")

        try:
            parsed_data = dict(parse_qsl(header))
        except ValueError:
            return None

        if "hash" not in parsed_data:
            return None

        data_hash = parsed_data.pop("hash")
        data_check_string = "\n".join(
            f"{key}={value}"
            for key, value in sorted(parsed_data.items(), key=itemgetter(0))
        )
        secret_key = hmac.new(
            key=b"WebAppData",
            msg=settings.BOT_TOKEN.encode(),
            digestmod=hashlib.sha256,
        )
        calculated_hash = hmac.new(
            key=secret_key.digest(),
            msg=data_check_string.encode(),
            digestmod=hashlib.sha256,
        ).hexdigest()

        # pk = eval(parsed_data["user"].replace("true", "True"))["id"]
        pk = json.loads(parsed_data["user"])["id"]

        if calculated_hash != data_hash:
            raise exceptions.AuthenticationFailed("Hash mismatch")

        user = get_user_or_none(pk=pk)
        return user, header
