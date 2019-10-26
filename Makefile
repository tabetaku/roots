.PHONY: all help

help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

# docker
docker-cmd: install-all run-server
docker-uwsgi-cmd: install-all run-uwsgi
docker-gunicorn-cmd: install-all run-gunicorn


# install
install-all: install-package settings collect-static

settings:
	@pipenv run make settings-internal

settings-internal:
	@cd src && python -m scripts.generate_secret -a default

cert:
	@cd docs/dev/cert \
	&& openssl req -new -newkey rsa:2048 -sha512 -nodes -keyout dev.key -out dev.csr -subj "/C=KR/ST=Seoul/L=Gang-nam/O=SecureSign Inc/OU=Dev Team/CN=example.com" \
	&& openssl x509 -req -days 3650 -sha512 -in dev.csr -signkey dev.key -out dev.crt

install-mysql:
	@apt update && apt install -y mysql-server default-libmysqlclient-dev

install-package:
	@pipenv install --dev
	# @pipenv update --dev

collect-static:
	@pipenv run python src/manage.py collectstatic --no-input --clear


# run
run-server:
	@pipenv run python src/manage.py runserver 0.0.0.0:8000

run-uwsgi:
	@pipenv run uwsgi --ini /htdocs/www/docs/wsgi/uwsgi/roots-django.ini --import infras.crontab

run-gunicorn:
	@pipenv run gunicorn -c /htdocs/www/docs/wsgi/gunicorn/roots-django.py sites.wsgi:application

shell:
	@pipenv shell

# test
test:
	@pipenv run python src/manage.py test src --noinput

# pre-processing
lint:
	@pipenv run pylint ./src/ --rcfile=.pylintrc
	@pipenv run flake8

# docker
docker-up:
	@docker-compose up

docker-rebuild-up:
	@docker-compose up --force-recreate --build

docker-kill-all:
	@docker ps -a -q | xargs docker rm -f

docker-logs:
	@docker-compose logs -f roots-django

docker-bash:
	@docker-compose exec roots-django /bin/bash
