.PHONY: all $(MAKECMDGOALS)
.SUFFIXES:

all: test

test:
	@python -m pytest

run:
	@python main.py