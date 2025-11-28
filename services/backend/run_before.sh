#!/bin/sh
echo "Start RUN_BEFORE"
pipenv run python3 run_before.py
pipenv run python3 manage.py collectstatic --noinput
pipenv run python3 manage.py makemigrations
pipenv run python3 manage.py migrate
echo "End RUN_BEFORE"