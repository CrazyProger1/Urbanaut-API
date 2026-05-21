import logging

from src.apps.accounts.events.args import UserCreatedEvent, UserReferralEvent, UserAchievementEvent, TeamCreatedEvent
from src.apps.accounts.services.achivements import give_default_achievements, give_achievement_for_referral, \
    give_achievement_for_team
from src.apps.accounts.services.rewards import reward_new_user, reward_user_referrer, reward_user_for_achievement
from src.apps.accounts.services.notifications import notify_user_referrer, notify_user_got_achievement

logger = logging.getLogger(__name__)


def handle_user_created(event: UserCreatedEvent):
    user = event.user

    give_default_achievements(user=user)
    reward_new_user(user=user)


def handle_user_referral(event: UserReferralEvent):
    user = event.user
    code = event.code

    reward_user_referrer(code=code)
    notify_user_referrer(code=code, referral=user)
    give_achievement_for_referral(user=code.created_by)


def handle_user_achievement(event: UserAchievementEvent):
    user = event.user
    achievement = event.achievement

    reward_user_for_achievement(user=user, achievement=achievement)
    notify_user_got_achievement(user=user, achievement=achievement)


def handle_team_created(event: TeamCreatedEvent):
    team = event.team
    give_achievement_for_team(team=team)
