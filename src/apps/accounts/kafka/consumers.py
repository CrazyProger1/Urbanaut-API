from src.apps.kafka.consumers import KafkaConsumer


class ReferralKafkaConsumer(KafkaConsumer):
    topic = "user.referral.apply"
    group_id = "referral_group"

    def handle(self, message) -> None:
        print(message, type(message), message.__dict__)
