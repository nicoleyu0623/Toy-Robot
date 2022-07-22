# @Time : 22/7/22 7:44 pm
# @Original Author : Nicole Yu
# @File : test_move.py
# @Project: AUTOMATION

import pytest

from src.allocation.domain.Robot import Robot
from src.allocation.domain.Position import Position
from src.allocation.domain.Direction import Direction


@pytest.mark.parametrize(
    "initial_position, initial_direction, expected_result",
    [
        (Position(0, 1), Direction.SOUTH, [0, 0]),
        (Position(0, 0), Direction.EAST, [1, 0]),
        (Position(1, 0), Direction.WEST, [0, 0]),
        (Position(0, 0), Direction.NORTH, [0, 1]),
    ],
)
def test_move(initial_position, initial_direction, expected_result):
    robot = Robot(initial_direction, initial_position)
    robot.move()
    result = [robot.current_position.x, robot.current_position.y]
    assert result == expected_result
