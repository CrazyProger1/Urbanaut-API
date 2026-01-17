import datetime
import json

from django_celery_beat.models import PeriodicTask, ClockedSchedule


def plan_execution(
    task_id: str,
    task: str,
    execute_at: datetime.datetime,
    args: tuple = (),
    kwargs: dict = None,
) -> PeriodicTask:
    schedule = ClockedSchedule.objects.create(clocked_time=execute_at)

    data = {
        "clocked": schedule,
        "name": task_id,
        "task": task,
        "enabled": True,
        "one_off": True,
    }

    if args:
        data["args"] = json.dumps(args)

    if kwargs:
        data["kwargs"] = json.dumps(kwargs)

    task = PeriodicTask.objects.filter(name=task_id).first()

    if task:
        task.delete()

    return PeriodicTask.objects.create(**data)
