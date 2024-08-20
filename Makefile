.PHONY: docker.up
docker.up:
	docker-compose -f docker-compose.yml up

.PHONY: docker.down
docker.down:
	docker-compose down

.PHONY: docker.bash
docker.bash:
	docker-compose exec web bash

.PHONY: docker.log
docker.log:
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