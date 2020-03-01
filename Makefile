install:
	@poetry install

lint:
	@poetry run flake8 gen_diff
	
test:
	poetry run pytest --cov --cov-report xml tests/