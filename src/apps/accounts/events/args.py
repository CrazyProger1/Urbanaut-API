from dataclasses import dataclass

from src.apps.accounts.models import User, ReferralCode, Achievement


@dataclass
class UserCreatedEvent:
    user: User


@dataclass
class UserReferralEvent:
    user: User
    code: ReferralCode


@dataclass
class UserAchievementEvent:
    user: User
    achievement: Achievement
