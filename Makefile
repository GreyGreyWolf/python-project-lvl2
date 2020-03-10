install:
	@poetry install

lint:
	@poetry run flake8 gen_diff
	
test:
	
	poetry run pytest --cov=gendiff tests/ --cov-report xml

