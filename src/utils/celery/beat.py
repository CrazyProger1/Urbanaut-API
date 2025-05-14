import datetime
import json

from django.conf import settings
from django_celery_beat.models import CrontabSchedule, PeriodicTask


def plan_task(
    task: str,
    name: str,
    time: datetime.datetime,
    args: tuple = (),
    kwargs: dict = None,
    remove_existing: bool = True,
):
    schedule, created = CrontabSchedule.objects.get_or_create(
        minute=time.minute,
        hour=time.hour,
        day_of_month=time.day,
        month_of_year=time.month,
        day_of_week="*",
        timezone=settings.TIME_ZONE,
    )

    try:
        PeriodicTask.objects.get(name=name).delete()
    except PeriodicTask.DoesNotExist:
        pass

    if remove_existing:
        PeriodicTask.objects.filter(name=name).delete()

    PeriodicTask.objects.create(
        crontab=schedule,
        name=name,
        task=task,
        kwargs=json.dumps(kwargs or {}),
        args=json.dumps(args),
        one_off=True,
    )
