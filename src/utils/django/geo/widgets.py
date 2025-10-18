from django.contrib.gis.geos import Polygon
from unfold.widgets import UnfoldAdminTextareaWidget


class ManualGeometryFieldWidget(UnfoldAdminTextareaWidget):
    def __init__(self, attrs=None):
        default_attrs = {
            'rows': 6,
            'placeholder': 'EWKT Format\nPOLYGON((lon1 lat1, lon2 lat2, lon3 lat3, lon1 lat1))\nPOINT (-74.41 40.71)',
        }
        if attrs:
            default_attrs.update(attrs)
        super().__init__(attrs=default_attrs)

    def value_from_datadict(self, data, files, name):
        wkt = data.get(name)
        if wkt and wkt.strip():
            try:
                # Assume EWKT (with optional SRID=4326 prefix); strip whitespace
                geom = Polygon.from_ewkt(wkt.strip())
                if geom.geom_type == 'Polygon':
                    return geom
            except Exception:
                pass
        return None
