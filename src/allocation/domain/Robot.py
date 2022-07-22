# @Time : 21/7/22 1:23 pm
# @Original Author : Nicole Yu
# @File : Robot.py
# @Project: AUTOMATION

from dataclasses import dataclass
from src.allocation.domain.Position import Position
from src.allocation.domain.Rotation import Rotation
from src.allocation.domain.Direction import Direction
from src.allocation.validations.verify import verify_position
from src.allocation.exceptions.OutOfRangeError import PositionNotInRangeError
from src.utils.log_util import LOGGER

""" Robot class

This module demonstrates the some properties and several capabilities owned by the robot.


Attributes:
    current_direction (Direction): the direction that robot facing.
    current_position (Position): the position that robot locates in the (4,4) square.

Methods:
    - rotate(self, rotation_input: Rotation)
    - move(self)
    - report(self)
    
"""


@dataclass
class Robot:
    _current_direction: Direction
    _current_position: Position

    @property
    def current_direction(self) -> Direction:
        return self._current_direction

    @property
    def current_position(self) -> Position:
        return self._current_position

    @current_direction.setter
    def current_direction(self, current_direction) -> None:
        self._current_direction = current_direction

    @current_position.setter
    def current_position(self, current_position) -> None:
        try:
            verify_position(current_position.x, current_position.y)
            self._current_position = current_position
        except PositionNotInRangeError:
            LOGGER.error("Unable to set position due to position not in range")

    def rotate(self, rotation_input: Rotation) -> None:
        """
        To rotate the robot instance to different directions that it is facing to.
        :param rotation_input: User input that used to rotate the robot
        :return: None
        """
        # rotate robot
        if self.current_direction == Direction.EAST:
            if rotation_input == Rotation.LEFT:
                self.current_direction = Direction.NORTH
            else:
                self.current_direction = Direction.SOUTH
        elif self.current_direction == Direction.WEST:
            if rotation_input == Rotation.LEFT:
                self.current_direction = Direction.SOUTH
            else:
                self.current_direction = Direction.NORTH
        elif self.current_direction == Direction.NORTH:
            if rotation_input == Rotation.LEFT:
                self.current_direction = Direction.WEST
            else:
                self.current_direction = Direction.EAST
        else:  # south
            if rotation_input == Rotation.LEFT:
                self.current_direction = Direction.EAST
            else:
                self.current_direction = Direction.WEST

    def move(self) -> None:
        """
        to move the position of the robot in the (4,4) square.
        :return: None
        """
        if self.current_direction == Direction.EAST:
            if self.current_position.x < 5:
                self.current_position.x += 1
        if self.current_direction == Direction.WEST:
            if self.current_position.x > 0:
                self.current_position.x -= 1
        if self.current_direction == Direction.NORTH:
            if self.current_position.y < 5:
                self.current_position.y += 1
        if self.current_direction == Direction.SOUTH:
            if self.current_position.y > 0:
                self.current_position.y -= 1

    def report(self) -> None:
        """
        print the location and direction of the robot to the console.
        :return: None
        """
        print(
            f"Output: {self.current_position.x},{self.current_position.y},{self.current_direction.value}"
        )
