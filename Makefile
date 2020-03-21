install:
	poetry install

lint:
	poetry run flake8 gendiff.py
	
test:
	poetry run pytest --cov=gen_diff tests/ --cov-report=xml
