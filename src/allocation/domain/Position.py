# @Time : 21/7/22 1:13 pm
# @Original Author : Nicole Yu
# @File : Position.py
# @Project: AUTOMATION
from dataclasses import dataclass

""" Position class

This module demonstrate the position that the robot locates. 
The construction class contains getter and setter.

Attributes:
    x (int): horizontal position
    y (int): vertical position
    
"""


@dataclass
class Position:
    _x: int
    _y: int

    @property
    def x(self) -> int:
        return self._x

    @property
    def y(self) -> int:
        return self._y

    @x.setter
    def x(self, x) -> None:
        self._x: int = x

    @y.setter
    def y(self, y) -> None:
        self._y: int = y
