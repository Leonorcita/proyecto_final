coverage:
	coverage run -m pytest
	coverage report -m

pytest: coverage

format: black .

lint:
	black --check .
	flake8