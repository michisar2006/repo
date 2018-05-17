 migrate:
	docker-compose run --rm web python src/manage.py makemigrations --settings=pollap.settings.local
	docker-compose run --rm web python src/manage.py migrate auth --settings=pollap.settings.local
	docker-compose run --rm web python src/manage.py migrate --settings=pollap.settings.local

statics:
	docker-compose run --rm web python src/manage.py collectstatic --no-input --settings=pollap.settings.local