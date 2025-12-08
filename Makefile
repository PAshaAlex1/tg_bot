.PHONY: install run test

install:
	uv pip install -e .

run:
	python -m bot.app

test:
	pytest tests/




