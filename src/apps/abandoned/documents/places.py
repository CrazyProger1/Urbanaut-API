from django_elasticsearch_dsl import Document, fields
from django_elasticsearch_dsl.registries import registry


@registry.register_document
class PlaceDocument(Document):
    class Index:
        name = "places"
        settings = {
            "number_of_shards": 1,
            "number_of_replicas": 1,
        }

        class Django:
            model = Place
            fields = [
                "id",
                "first_name",
                "last_name",
                "username",
            ]
