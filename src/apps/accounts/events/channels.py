from src.apps.accounts.events.args import UserCreatedEvent, UserReferralEvent, UserAchievementEvent
from src.utils.events import EventChannel, Event


class UserEventChannel(EventChannel):
    user_created = Event[UserCreatedEvent]()
    user_referral = Event[UserReferralEvent]()
    user_achievement = Event[UserAchievementEvent]()
