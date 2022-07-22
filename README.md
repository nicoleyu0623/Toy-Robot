# Toy-Robot

A command line program simulates toy robot moving on a 4x4 square tabletop.
User/Player is supposed to interact with the terminal to give instruction to the toy.
Only valid instructions will let the robot move in the 4x4 square.

- The robot able to turn `LEFT` and `RIGHT`.
- The directions the robot able to face are: `NORTH`, `SOUTH`, `EAST` and `WEST`
- Robot only able to move vertically and horizontally.

## Requirements

- Docker
- a local python3.7 (at least) virtualenv

- (This application was developed on macOS Monterey 12.0.1)

## Building the containers

```bash
# build the python3.7 docker image and get into the interactive mode
make build
```
execute the program inside the container 
```bash
cd .. # go the parent folder of /src/
python3.7 -m src.bin.place_robot
```


## Creating a local virtualenv (optional)

```bash
python3.7 -m venv .venv && source .venv/bin/activate # or however you like to create virtualenvs

pip3 install -r requirements.txt

cd ~/Toy-Robot

python3.7 -m src.bin.place_robot
```

## Running the tests

```bash
make test
# or, to run individual test types
make unit-tests
make integration-tests
make e2e-tests
# or, if you have a local virtualenv
pytest tests/unit
pytest tests/integration
pytest tests/e2e
```

## Makefile

There are more useful commands in the makefile
