
# server

upserver:
	uvicorn app.main:app --reload


# redis

upredis:
	docker run --name redis-container -d \
		-p 6379:6379 \
		redis-image
downredis:
	docker stop redis-container
	docker rm redis-container


# celery

upcelery:
	celery -A app.tasks.celery_app:celery worker --loglevel=info --pool=solo

upflower:
	celery -A app.tasks.celery_app:celery flower


# database

updb:
	docker run --name db-container -d \
		-p 5432:5432 \
		-v booking_course:/var/lib/postgresql/data \
		db-image

downdb:
	docker stop db-container
	docker rm db-container


# migrations

init_migrations:
	alembic init migrations

migrations:
	alembic revision --autogenerate -m "$(filter-out $@,$(MAKECMDGOALS))"

migrate:
	alembic upgrade head



# lint

lint:
	isort .
	black --config pyproject.toml .
	flake8 --config setup.cfg

check_lint:
	isort --check --diff .
	flake8 --config setup.cfg
	autoflake -c -r --quiet .
	black --check --color --config pyproject.toml .
	pyright .



upsmtp:
	python -m smtpd -c DebuggingServer -n localhost:1025