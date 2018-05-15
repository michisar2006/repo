 migrate:
	docker-compose run --rm web python src/manage.py makemigrations --settings=pollap.settings.local
	docker-compose run --rm web python src/manage.py migrate auth --settings=pollap.settings.local
	docker-compose run --rm web python src/manage.py migrate --settings=pollap.settings.local