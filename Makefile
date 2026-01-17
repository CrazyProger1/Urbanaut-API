.PHONY: cleancode
cleancode:
	uv run black .
	uv run mypy .

.PHONY: run
run:
	uv run python manage.py runserver 8001


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