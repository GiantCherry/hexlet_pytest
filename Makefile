install:
	uv sync

run:
	uv run hexlet-pytest 100

test:
	uv run pytest

test-coverage:
	uv run pytest --cov=hexlet_pytest --cov-report xml

lint:
	uv run ruff check

check: test lint

build:
	uv build

.PHONY: install test lint selfcheck check build
