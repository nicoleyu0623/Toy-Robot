# @Time : 22/7/22 5:16 pm
# @Original Author : Nicole Yu
# @File : test_multi_instructions.py
# @Project: AUTOMATION
import pytest

from src.allocation.domain.Robot import Robot
from src.allocation.domain.Position import Position
from src.allocation.domain.Direction import Direction
from src.allocation.domain.Rotation import Rotation


def test_instructions_sets_one():
    robot = Robot(Direction.SOUTH, Position(0, 2))
    robot.move()
    robot.move()
    assert robot.current_position == Position(0, 0) and robot.current_direction == Direction.SOUTH


def test_instructions_set_two():
    robot = Robot(Direction.EAST, Position(1, 2))
    robot.move()
    robot.move()
    robot.rotate(Rotation.LEFT)
    robot.move()
    robot.move()
    print(robot.current_position)
    assert robot.current_position == Position(3, 4) and robot.current_direction == Direction.NORTH


def test_instructions_set_three():
    robot = Robot(Direction.NORTH, Position(3, 1))
    robot.move()
    robot.move()
    robot.rotate(Rotation.LEFT)
    robot.rotate(Rotation.RIGHT)
    robot.rotate(Rotation.LEFT)
    robot.move()
    robot.move()
    assert robot.current_position == Position(1, 3) and robot.current_direction == Direction.WEST
