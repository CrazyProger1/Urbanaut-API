from unittest.mock import patch

from django.contrib.auth import get_user_model
from django.contrib.gis.geos import Point, Polygon
from django.db import connection
from rest_framework.test import APITestCase

from src.apps.abandoned.enums import PreservationLevel, SecurityLevel
from src.apps.abandoned.models import Place, Area, UserFavoritePlace
from src.apps.geo.models import Country, Address
from src.apps.tags.models import Tag

User = get_user_model()

LIST_URL = "/api/v1/places/"


class PlaceAPITestCase(APITestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        with connection.cursor() as cursor:
            cursor.execute("CREATE EXTENSION IF NOT EXISTS pg_trgm")

    def setUp(self):
        self.user = User.objects.create_user(
            email="test@example.com",
            password="testpass123",
        )
        self.client.force_authenticate(user=self.user)

    def _ids(self, response):
        return [p["id"] for p in response.data["results"]]

    def test_filter_by_name(self):
        place_alpha = Place.objects.create(name="Alpha", point=Point(30.0, 50.0), created_by=self.user)
        place_beta = Place.objects.create(name="Beta", point=Point(11.0, 21.0), created_by=self.user)

        response = self.client.get(LIST_URL, {"name": "Alpha"})

        self.assertEqual(response.status_code, 200)
        ids = self._ids(response)
        self.assertIn(place_alpha.id, ids)
        self.assertNotIn(place_beta.id, ids)

    def test_filter_by_area(self):
        polygon = Polygon.from_bbox((29.0, 49.0, 32.0, 52.0))
        area = Area.objects.create(name="Zone", polygon=polygon)
        place_in_area = Place.objects.create(name="In Area", point=Point(30.0, 50.0), created_by=self.user, area=area)
        place_no_area = Place.objects.create(name="No Area", point=Point(11.0, 21.0), created_by=self.user)

        response = self.client.get(LIST_URL, {"area": area.pk})

        self.assertEqual(response.status_code, 200)
        ids = self._ids(response)
        self.assertIn(place_in_area.id, ids)
        self.assertNotIn(place_no_area.id, ids)

    def test_filter_by_tags(self):
        tag = Tag.objects.create(tag="urban")
        place_tagged = Place.objects.create(name="Tagged", point=Point(30.0, 50.0), created_by=self.user)
        place_tagged.tags.add(tag)
        place_untagged = Place.objects.create(name="Untagged", point=Point(11.0, 21.0), created_by=self.user)

        response = self.client.get(LIST_URL, {"tags": "urban"})

        self.assertEqual(response.status_code, 200)
        ids = self._ids(response)
        self.assertIn(place_tagged.id, ids)
        self.assertNotIn(place_untagged.id, ids)

    def test_filter_by_query(self):
        place_match = Place.objects.create(name="Abandoned Factory", point=Point(30.0, 50.0), created_by=self.user)
        place_no_match = Place.objects.create(name="Xyzzy Nothing", point=Point(11.0, 21.0), created_by=self.user)

        response = self.client.get(LIST_URL, {"query": "factory"})

        self.assertEqual(response.status_code, 200)
        ids = self._ids(response)
        self.assertIn(place_match.id, ids)
        self.assertNotIn(place_no_match.id, ids)

    def test_filter_by_ai_query(self):
        place_match = Place.objects.create(name="Ghostly Hospital", point=Point(30.0, 50.0), created_by=self.user)
        place_no_match = Place.objects.create(name="Other Place", point=Point(11.0, 21.0), created_by=self.user)

        with patch(
            "src.apps.abandoned.filters.places.search_places_ai",
            return_value=Place.objects.filter(pk=place_match.pk),
        ):
            response = self.client.get(LIST_URL, {"ai_query": "hospital"})

        self.assertEqual(response.status_code, 200)
        ids = self._ids(response)
        self.assertIn(place_match.id, ids)
        self.assertNotIn(place_no_match.id, ids)

    def test_filter_by_preservation(self):
        place_high = Place.objects.create(name="Well Preserved", point=Point(30.0, 50.0), created_by=self.user)
        preservation = place_high.preservation
        preservation.has_roof = True            # +3
        preservation.has_floor = True           # +2
        preservation.has_walls = True           # +2
        preservation.has_internal_ceilings = True  # +2  → total 9 → HIGH
        preservation.save()

        place_none = Place.objects.create(name="Ruins", point=Point(11.0, 21.0), created_by=self.user)

        response = self.client.get(LIST_URL, {"preservation": PreservationLevel.HIGH})

        self.assertEqual(response.status_code, 200)
        ids = self._ids(response)
        self.assertIn(place_high.id, ids)
        self.assertNotIn(place_none.id, ids)

    def test_filter_by_security(self):
        place_secured = Place.objects.create(name="Secured Place", point=Point(30.0, 50.0), created_by=self.user)
        security = place_secured.security
        security.has_security = True
        security.has_dogs = True  # score=3 → MEDIUM
        security.save()

        place_open = Place.objects.create(name="Open Place", point=Point(11.0, 21.0), created_by=self.user)

        response = self.client.get(LIST_URL, {"security": SecurityLevel.MEDIUM})

        self.assertEqual(response.status_code, 200)
        ids = self._ids(response)
        self.assertIn(place_secured.id, ids)
        self.assertNotIn(place_open.id, ids)

    def test_filter_by_has_security(self):
        place_guarded = Place.objects.create(name="Guarded", point=Point(30.0, 50.0), created_by=self.user)
        security = place_guarded.security
        security.has_security = True
        security.save()

        place_open = Place.objects.create(name="Open", point=Point(11.0, 21.0), created_by=self.user)

        response = self.client.get(LIST_URL, {"has_security": "true"})

        self.assertEqual(response.status_code, 200)
        ids = self._ids(response)
        self.assertIn(place_guarded.id, ids)
        self.assertNotIn(place_open.id, ids)

    def test_filter_by_country(self):
        country = Country.objects.create(name="Ukraine", continent="EU", tld="ua")
        address = Address.objects.create(country=country)
        place_ua = Place.objects.create(name="Ukrainian Place", point=Point(30.0, 50.0), created_by=self.user, address=address)
        place_no_country = Place.objects.create(name="No Country", point=Point(11.0, 21.0), created_by=self.user)

        response = self.client.get(LIST_URL, {"country": "ua"})

        self.assertEqual(response.status_code, 200)
        ids = self._ids(response)
        self.assertIn(place_ua.id, ids)
        self.assertNotIn(place_no_country.id, ids)

    def test_filter_by_is_favorite(self):
        place_fav = Place.objects.create(name="Favorite", point=Point(30.0, 50.0), created_by=self.user)
        UserFavoritePlace.objects.create(user=self.user, place=place_fav)
        place_not_fav = Place.objects.create(name="Not Favorite", point=Point(11.0, 21.0), created_by=self.user)

        response = self.client.get(LIST_URL, {"is_favorite": "true"})

        self.assertEqual(response.status_code, 200)
        ids = self._ids(response)
        self.assertIn(place_fav.id, ids)
        self.assertNotIn(place_not_fav.id, ids)

    def test_filter_by_is_private(self):
        place_private = Place.objects.create(name="Private", point=Point(30.0, 50.0), created_by=self.user, is_private=True)
        place_public = Place.objects.create(name="Public", point=Point(11.0, 21.0), created_by=self.user)

        response = self.client.get(LIST_URL, {"is_private": "true"})

        self.assertEqual(response.status_code, 200)
        ids = self._ids(response)
        self.assertIn(place_private.id, ids)
        self.assertNotIn(place_public.id, ids)

    def test_filter_by_is_supposed(self):
        place_supposed = Place.objects.create(name="Supposed", point=Point(30.0, 50.0), created_by=self.user, is_supposed=True)
        place_regular = Place.objects.create(name="Regular", point=Point(11.0, 21.0), created_by=self.user)

        response = self.client.get(LIST_URL, {"is_supposed": "true"})

        self.assertEqual(response.status_code, 200)
        ids = self._ids(response)
        self.assertIn(place_supposed.id, ids)
        self.assertNotIn(place_regular.id, ids)
