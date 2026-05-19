from src.apps.accounts.views.oauth import (
    GoogleOauthRedirectURIView,
    GoogleOauthCallbackView,
)
from src.apps.accounts.views.settings import SettingsViewSet
from src.apps.accounts.views.referrals import ReferralCodeViewSet, ReferralsViewSet
from src.apps.accounts.views.users import UserViewSet, UserByUsernameViewSet
from src.apps.accounts.views.tokens import WebsocketTokenCreateView
from src.apps.accounts.views.languages import LanguageListAPIView
from src.apps.accounts.views.teams import TeamViewSet
from src.apps.accounts.views.members import TeamMemberViewSet
from src.apps.accounts.views.achievements import AchievementViewSet
