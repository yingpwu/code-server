dev:
	FLASK_APP=main flask run

test:
	pytest

coverage:
	pytest --cov=. --cov-report term-missing --cov-report xml tests/*

.PHONY: dev test coverage