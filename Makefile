all: sdist

sdist:
	python3 setup.py sdist

upload:
	twine upload dist/*

mypy:
	python3 -m mypy cryptologic/cryptologic.py

test:
	python3 -m pytest --mypy --cov=cryptologic tests/

.PHONY: sdist upload mypy test
