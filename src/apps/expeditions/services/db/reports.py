from src.apps.expeditions.models import Report


def get_all_reports():
    return Report.objects.all()
