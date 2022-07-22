# @Time : 22/7/22 7:57 pm
# @Original Author : Nicole Yu
# @File : test_final_reports.py
# @Project: AUTOMATION


"""
Capture IO STDOUT
"""

import sys

from src.allocation.domain.Robot import Robot
from src.allocation.domain.Position import Position
from src.allocation.domain.Direction import Direction
from src.allocation.domain.Rotation import Rotation


def test_e2e_instructions_sets_one(capsys):
    robot = Robot(Direction.SOUTH, Position(0, 3))
    robot.move()
    robot.move()
    robot.report()
    captured = capsys.readouterr()
    assert captured.out == "Output: 0,1,SOUTH\n"


def test_e2e_instructions_sets_two(capsys):
    robot = Robot(Direction.NORTH, Position(0, 0))
    robot.rotate(Rotation.LEFT)
    robot.report()
    captured = capsys.readouterr()
    assert captured.out == "Output: 0,0,WEST\n"


def test_e2e_instructions_sets_three(capsys):
    robot = Robot(Direction.EAST, Position(1, 2))
    robot.move()
    robot.move()
    robot.rotate(Rotation.LEFT)
    robot.move()
    robot.report()
    captured = capsys.readouterr()
    assert captured.out == "Output: 3,3,NORTH\n"
