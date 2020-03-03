install:
	@poetry install

lint:
	@poetry run flake8 gen_diff
	
test:
	python3 -m poetry run pytest --cov --cov-report xml tests/