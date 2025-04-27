from kafka.consumer.fetcher import ConsumerRecord

from src.apps.accounts.services.db import get_user_or_none
from src.apps.accounts.services.db.referrals import (
    get_referral_link_or_none,
    apply_referral_link,
)
from src.apps.kafka.consumers import KafkaConsumer


class ReferralKafkaConsumer(KafkaConsumer):
    topic = "user.referral.apply"
    group_id = "referral_group"

    def handle(self, message: ConsumerRecord) -> None:
        value = message.value
        user_id = value["user_id"]
        code = value["code"]
        user = get_user_or_none(id=user_id)
        link = get_referral_link_or_none(code=code)
        apply_referral_link(
            user=user,
            link=link,
        )
