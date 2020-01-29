.PHONY: docs

init:
	pip install poetry
	poetry install

reinit:
	poetry env remove python
	make init

test:
	poetry run pytest

lock:
	poetry export -f requirements.txt -o requirements.txt

coverage:
	poetry run pytest --cov=enigma tests/ --cov-report=html
