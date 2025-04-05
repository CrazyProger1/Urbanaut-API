import asyncio
import logging
from asyncio import Semaphore
from typing import Iterable

from aiogram import Bot
from aiogram.enums import ParseMode
from django.conf import settings

logger = logging.getLogger(__name__)


async def asend_newsletter(
        message: str,
        user_ids: Iterable[int]
):
    user_ids = set(user_ids)
    bot = Bot(
        token=settings.TELEGRAM_BOT_TOKEN,
        parse_mode=ParseMode.HTML,
    )
    sent_count = 0
    failed_count = 0
    total_count = len(user_ids)

    async def send_message(user_id: int):
        nonlocal sent_count, failed_count

        async with semaphore:
            try:
                await bot.send_message(
                    chat_id=user_id,
                    text=message,
                )
                sent_count += 1
                logger.debug("Message sent to user №%s", user_id)
            except Exception as e:
                logger.warning("Failed to send message to user №%s: %s", user_id, e)
                failed_count += 1

            await asyncio.sleep(1 / settings.TELEGRAM_RATE_PER_SECOND_SENDING)

    semaphore = Semaphore(value=settings.TELEGRAM_RATE_PER_SECOND_SENDING)
    tasks = [send_message(user_id=user_id) for user_id in user_ids]
    await asyncio.gather(*tasks)
