.DEFAULT_GOAL := server

shell:
	python3 manage.py shell_plus --ipython

server:
	python manage.py runserver

mm:
	python manage.py makemigrations

migrate:
	python manage.py migrate

setup:
	python3 -m venv dpassvenv
	. ./dpassvenv/bin/activate
	python3 -m pip install -r ./requirements/dev_requirements.txt