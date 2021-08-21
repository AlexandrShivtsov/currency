SHELL := /bin/bash

manage_py := python app/manage.py

runserver:
	$(manage_py) runserver

worker:
	#cd app && celery -A settings worker -l info --autoscale=2,1
	cd app && celery -A settings worker -l info --concurrency 10

beat:
	cd app && celery -A settings beat -l info

shell:
	$(manage_py) shell

makemigrations:
	$(manage_py) makemigrations

migrate:
	$(manage_py) migrate
    	
