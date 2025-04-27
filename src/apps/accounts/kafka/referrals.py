import logging

from django.conf import settings
from kafka.consumer.fetcher import ConsumerRecord

from src.apps.accounts.services.db import get_user_or_none
from src.apps.accounts.services.db.referrals import (
    get_referral_link_or_none,
    apply_referral_link,
)
from src.apps.kafka.consumers import KafkaConsumer

logger = logging.getLogger(__name__)


class ReferralKafkaConsumer(KafkaConsumer):
    topic = settings.KAFKA_TOPIC_APPLY_REFERRAL
    group_id = settings.KAFKA_GROUP_REFERRAL

    def handle(self, message: ConsumerRecord) -> None:
        try:
            value = message.value
            user_id = value["user_id"]
            code = value["code"]
            user = get_user_or_none(id=user_id)

            if not user:
                logger.warning("Failed to find user: %s", user_id)
                return

            link = get_referral_link_or_none(code=code)

            if not link:
                logger.warning("Failed to find referral link with code: %s", code)
                return

            is_applied = apply_referral_link(
                user=user,
                link=link,
            )
            if not is_applied:
                logger.warning("Failed to apply referral link: %s", link)
                return

            logger.info("Successfully applied referral link: %s", link)
        except Exception as e:
            logger.warning(f"Failed to handle %s. Got %s", self.topic, message.value, exc_info=e)
