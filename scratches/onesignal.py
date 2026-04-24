import asyncio
import os

from onesignal_sdk.client import AsyncClient
from django import setup

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "src.config.settings")
setup()

from django.conf import settings


async def main():
    client = AsyncClient(
        app_id=settings.ONESIGNAL_APP_ID,
        rest_api_key=settings.ONESIGNAL_API_KEY,
    )

    # Use external user ID (your own user ID, like Django User UUID)
    # This is the recommended approach for production
    external_user_id = "5293e42a-45c8-4741-9af8-999fbedd6222"

    notification_body = {
        "include_external_user_ids": [external_user_id],
        "contents": {
            "en": "Hello, world",
            "es": "Hola mundo",
            "fr": "Bonjour le monde",
            "zh-Hans": "你好世界",
        },
    }

    print(f"Sending notification to external user ID: {external_user_id}")
    response = await client.send_notification(notification_body)
    print(f"Response: {response.body}")


if __name__ == "__main__":
    asyncio.run(main())
