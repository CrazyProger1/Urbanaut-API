import src.apps.notifier.i18n
from src.apps.notifier.admin.notifications import (
    NotificationAdmin,
    NotificationStatusAdmin,
)
from src.apps.notifier.admin.newsletters import NewsletterAdmin
from src.apps.notifier.admin.events import EventAdmin
from src.apps.notifier.admin.categories import CategoryAdmin, CategoryRecipientInline
from src.apps.notifier.admin.beat import (
    SolarScheduleAdmin,
    ClockedScheduleAdmin,
    CrontabScheduleAdmin,
    IntervalScheduleAdmin,
    PeriodicTaskAdmin,
)
