# @Time : 22/7/22 7:44 pm
# @Original Author : Nicole Yu
# @File : test_rotation.py
# @Project: AUTOMATION


import pytest

from src.allocation.domain.Robot import Robot
from src.allocation.domain.Position import Position
from src.allocation.domain.Direction import Direction
from src.allocation.domain.Rotation import Rotation


@pytest.mark.parametrize(
    "initial_position, initial_direction, expected_result",
    [
        (Position(0, 1), Direction.SOUTH, Direction.EAST),
        (Position(2, 4), Direction.EAST, Direction.NORTH),
        (Position(3, 1), Direction.WEST, Direction.SOUTH),
        (Position(4, 4), Direction.NORTH, Direction.WEST),
    ],
)
def test_rotate_left(initial_position, initial_direction, expected_result):
    robot = Robot(initial_direction, initial_position)
    robot.rotate(Rotation("LEFT"))
    result = robot.current_direction
    assert result == expected_result


@pytest.mark.parametrize(
    "initial_position, initial_direction, expected_result",
    [
        (Position(4, 4), Direction.SOUTH, Direction.WEST),
        (Position(3, 4), Direction.EAST, Direction.SOUTH),
        (Position(1, 2), Direction.WEST, Direction.NORTH),
        (Position(4, 3), Direction.NORTH, Direction.EAST),
    ],
)
def test_rotate_right(initial_position, initial_direction, expected_result):
    robot = Robot(initial_direction, initial_position)
    robot.rotate(Rotation("RIGHT"))
    result = robot.current_direction
    assert result == expected_result
