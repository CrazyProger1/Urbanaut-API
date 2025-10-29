from src.apps.abandoned.models import Area, Place


def get_all_areas():
    return Area.objects.all()


def get_parent_area(area: Area):
    return


def get_place_area_or_none(place: Place) -> Area | None:
    point = place.point

    areas = Area.objects.filter(polygon__contains=point)

    # TODO: improve logic (can be top-level parent area)
    return areas.first()
