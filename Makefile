.PHONY: docker.up
docker.up:
	docker-compose -f docker-compose.yml up --detach


.PHONY: docker.up.build
docker.up.build:
	docker-compose -f docker-compose.yml up --detach --build


.PHONY: docker.down
docker.down:
	docker-compose down

.PHONY: docker.bash
docker.bash:
	docker-compose exec api bash

.PHONY: docker.log
docker.log:
	docker container logs web --follow

.PHONY: cleancode
cleancode:
	black .
	mypy .

.PHONY: db.migrations
db.migrations:
	python manage.py makemigrations


.PHONY: db.migrate
db.migrate:
	python manage.py migrate


.PHONY: db.superuser
db.superuser:
	python manage.py createsuperuser --no-input

