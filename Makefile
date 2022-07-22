
PYTHON = python3.7

.PHONY = help setup test run clean

.DEFAULT_GOAL = help

help:
	echo "---------------HELP-----------------"
	echo "To test the project type make test"
	echo "To run the project type make run"
	echo "To format the project type make black"
	echo "------------------------------------"

build:
	docker build -t toy-robot .
	docker run -it --tty toy-robot /bin/bash

run:
	${PYTHON} -m src.bin.place_robot

test:
	${PYTHON} -m pytest tests/e2e tests/exceptions tests/integration tests/unit tests/validations

unit-tests:
	${PYTHON} -m pytest tests/unit

integration-tests:
	${PYTHON} -m pytest tests/integration

e2e-tests:
	${PYTHON} -m pytest tests/e2e

black:
	black -l 86 $(find * -name '*.py')
