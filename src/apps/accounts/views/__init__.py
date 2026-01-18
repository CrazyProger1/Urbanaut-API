from src.apps.accounts.views.oauth import (
    GoogleOauthRedirectURIView,
    GoogleOauthCallbackView,
)
from src.apps.accounts.views.settings import SettingsViewSet
from src.apps.accounts.views.referrals import ReferralCodeViewSet
from src.apps.accounts.views.users import UserViewSet, UserByUsernameViewSet
from src.apps.accounts.views.tokens import WebsocketTokenCreateView
