.DEFAULT_GOAL := server

shell:
	python3 manage.py shell_plus --ipython

server:
	python manage.py runserver

mm:
	python manage.py makemigrations

migrate:
	python manage.py migrate

superuser:
	python manage.py createsuperuser
