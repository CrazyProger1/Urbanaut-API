.PHONY: cleancode
cleancode:
	uv run black .
	uv run mypy .

.PHONY: run
run:
	uv run python manage.py runserver 8001


.PHONY: worker
worker:
	uv run celery -A src.config.settings.celery worker -l INFO


.PHONY: beat
beat:
	uv run celery -A src.config.settings.celery beat -l INFO --scheduler django_celery_beat.schedulers:DatabaseScheduler



.PHONY: db.migrations
db.migrations:
	uv run python manage.py makemigrations


.PHONY: db.migrate
db.migrate:
	uv run python manage.py migrate


.PHONY: db.superuser
db.superuser:
	uv run python manage.py createsuperuser --no-input


.PHONY: shell
shell:
	uv run python manage.py shell


.PHONY: test
test:
	uv run pytest .


BABEL_KEYWORDS = -k gettext_lazy -k gettext_noop -k ngettext_lazy:1,2 -k pgettext_lazy:1c,2 -k npgettext_lazy:1c,2,3
BABEL_DOMAIN = django
BABEL_LOCALES_DIR = locales
BABEL_POT = $(BABEL_LOCALES_DIR)/messages.pot
BABEL_LANGUAGES = en uk ru

.PHONY: i18n.extract
i18n.extract:
	uv run pybabel extract -F babel.cfg $(BABEL_KEYWORDS) -o $(BABEL_POT) .

.PHONY: i18n.init
i18n.init:
	$(foreach lang,$(BABEL_LANGUAGES),uv run pybabel init -i $(BABEL_POT) -d $(BABEL_LOCALES_DIR) -D $(BABEL_DOMAIN) -l $(lang);)

.PHONY: i18n.update
i18n.update:
	uv run pybabel update -i $(BABEL_POT) -d $(BABEL_LOCALES_DIR) -D $(BABEL_DOMAIN)

.PHONY: i18n.compile
i18n.compile:
	uv run pybabel compile -d $(BABEL_LOCALES_DIR) -D $(BABEL_DOMAIN)