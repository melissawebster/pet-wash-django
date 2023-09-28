venv:
	venv\Scripts\activate

run:
	python manage.py runserver 9000

migrate:
	python manage.py makemigrations && python manage.py migrate


#pytest
