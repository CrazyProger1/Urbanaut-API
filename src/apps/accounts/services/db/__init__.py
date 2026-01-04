from src.apps.accounts.services.db.settings import get_all_settings
from src.apps.accounts.services.db.users import get_or_create_user
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
