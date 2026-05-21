from dataclasses import dataclass

from src.apps.accounts.models import User, ReferralCode, Achievement, Team


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


@dataclass
class TeamCreatedEvent:
    team: Team
