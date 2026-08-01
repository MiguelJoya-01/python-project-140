install:
	uv sync

build:
	uv build

package-install:
	uv tool install dist/*.whl

brain-games:
	uv run brain-games

brain-even:
	uv run brain-even

lint:
	uv run ruff check .

clean:
	rm -rf dist *.egg-info .venv
