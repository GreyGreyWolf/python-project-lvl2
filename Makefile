install:
	@poetry install

lint:
	@poetry run flake8 gen_diff
	
test:
	
	poetry run pytest --cov=gen_diff tests/ --cov-report xml

