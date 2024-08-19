.PHONY: docker.up
docker.up:
	docker-compose --build -d -f compose.dev.yaml up

.PHONY: docker.down
docker.down:
	docker-compose down

.PHONY: docker.bash
docker.bash:
	docker-compose exec web bash

.PHONY: docker.log
docker.bash:
	docker container logs web --follow

.PHONY: cleancode
cleancode:
	black .
	mypy .

.PHONY: migrations
migrations:
	python manage.py makemigrations


.PHONY: migrate
migrate:
	python manage.py migrate


.PHONY: superuser
superuser:
	python manage.py createsuperuser --no-input