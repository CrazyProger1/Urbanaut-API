from django.contrib.gis import measure, geos
from django.contrib.gis.db.models import functions
from rest_framework import filters, exceptions


class DistanceOrderingBackend(filters.BaseFilterBackend):
    max_distance_param: str = "max_distance"
    point_param: str = "point"
    srid: int = 4326

    def get_ref_point(self, request, **kwargs):
        point_string = request.query_params.get(self.point_param, None)
        if not point_string:
            return None

        try:
            lat, lon = map(float, point_string.split(","))
        except ValueError:
            raise exceptions.ParseError(
                "Invalid geometry string supplied for parameter {0}".format(
                    self.point_param
                )
            )

        return geos.Point(lon, lat, **kwargs)

    def filter_queryset(self, request, queryset, view):
        dest_point_field = getattr(view, "point_field", None)
        max_distance = str(request.query_params.get(self.max_distance_param))

        if not dest_point_field:
            return queryset

        ref_point = self.get_ref_point(request=request, srid=self.srid)
        if not ref_point:
            return queryset

        if max_distance.isdigit():
            queryset = queryset.filter(
                **{
                    f"{dest_point_field}__distance_lte": (
                        ref_point,
                        measure.Distance(km=int(max_distance)),
                    )
                }
            )

        queryset.annotate(
            distance=functions.Distance(dest_point_field, ref_point)
        ).order_by("distance")

        return queryset

    def get_schema_operation_parameters(self, view):
        return [
            {
                "name": self.max_distance_param,
                "required": False,
                "in": "query",
                "schema": {"type": "number", "format": "float", "default": None},
                "description": f"Maximum distance.",
            },
            {
                "name": self.point_param,
                "required": False,
                "in": "query",
                "description": "Coordinates (lat, lon).",
                "schema": {
                    "type": "array",
                    "items": {
                        "type": "number",
                        "format": "float"
                    },
                    "minItems": 2,
                    "maxItems": 2,

                    "example": [0, 10]
                },
                "style": "form",
                "explode": False,
            },
        ]
