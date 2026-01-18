from src.apps.accounts.services.db.settings import get_all_settings
from src.apps.accounts.services.db.users import (
    get_or_create_user_by_email,
    count_users,
    get_all_users,
    set_user_country,
    get_user_by_username_or_none,
    get_user_or_none,
)
from src.apps.accounts.services.db.referrals import (
    get_all_referral_codes,
    get_user_referral_codes,
    apply_referral_code,
    get_referral_code_or_none,
)
from src.apps.accounts.services.db.achievements import (
    get_achievement_or_none_by_slug,
    give_achievement,
)
from src.apps.accounts.services.db.usernames import (
    has_username,
    get_username_or_none,
    give_username,
    give_initial_username,
)
from src.apps.accounts.services.db.referrals import (
    has_referral_code,
    give_initial_referral_code,
)
