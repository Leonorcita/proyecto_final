coverage:
	coverage run -m pytest
	coverage report -m

pytest: coverage