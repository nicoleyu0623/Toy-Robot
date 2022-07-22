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



### Folder Structure
```bash
├── Dockerfile
├── LICENSE
├── Makefile
├── README.md
├── Toy-Robot-Code-Challenge-2022.pdf
├── requirements.txt
├── src
│   ├── __init__.py
│   ├── allocation
│   │   ├── __init__.py
│   │   ├── domain
│   │   │   ├── Direction.py
│   │   │   ├── Instructions.py
│   │   │   ├── Position.py
│   │   │   ├── Robot.py
│   │   │   ├── Rotation.py
│   │   │   ├── __init__.py
│   │   ├── exceptions
│   │   │   ├── OutOfRangeError.py
│   │   │   ├── __init__.py
│   │   └── validations
│   │       ├── __init__.py
│   │       └── verify.py
│   ├── bin
│   │   ├── __init__.py
│   │   └── place_robot.py
│   └── utils
│       ├── __init__.py
│       └── log_util.py
└── tests
    ├── __init__.py
    ├── e2e
    │   └── test_final_reports.py
    ├── exceptions
    │   └── test_exceptions.py
    ├── integration
    │   └── test_multi_instructions.py
    ├── unit
    │   ├── test_move.py
    │   ├── test_robot.py
    │   └── test_rotation.py
    └── validations
         └── test_validations.py
```

## Log files
- under project folder `toy-robot.log`

### Sample input & output
```bash
▶ python3 -m src.bin.place_robot

Please enter your instruction: <enter>
place 0,1,north
Please enter your instruction: <enter>
move
Please enter your instruction: <enter>
report
Output: 0,2,NORTH


```
