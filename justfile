# https://just.systems

install:
    uv sync --all-extras

lint:
    uv run ruff format .
    uv run ruff check --fix .
    uv run mypy authmoderne/ tests/

lint-check:
    uv run ruff format --check .
    uv run ruff check .
    uv run mypy authmoderne/ tests/

test:
    uv run pytest

test-cov-xml:
    uv run pytest --cov-report=xml

docs-serve:
    rm -rf trace.json site/ .cache/
    uv run zensical serve

docs-build:
    uv run zensical build --clean

version bump:
    uvx hatch version {{bump}}
