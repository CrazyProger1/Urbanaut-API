from decouple import config

ELASTICSEARCH_HOST = config("ELASTICSEARCH_HOST", default="localhost")
ELASTICSEARCH_PORT = config("ELASTICSEARCH_PORT", default=9200)

ELASTICSEARCH_DSL = {
    "default": {"hosts": f"{ELASTICSEARCH_HOST}:{ELASTICSEARCH_PORT}"},
}
