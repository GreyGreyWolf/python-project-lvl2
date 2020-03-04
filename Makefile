install:
	python3 -m poetry install

lint:
	python3 -m poetry run flake8 gen_diff
	
test:
	python3 -m poetry run pytest --cov=gen_diff tests/ --cov-report xml