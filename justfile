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
    uv run mkdocs serve -w docs/ -w mkdocs.yml --watch-theme

docs-build:
    uv run mkdocs build

version bump:
    uvx hatch version {{bump}}
