# @Time : 21/7/22 1:09 pm
# @Original Author : Nicole Yu
# @File : Direction.py
# @Project: AUTOMATION

from enum import Enum

""" Direction class

This modules enumerate the direction that the robot could face to. 
All the direction are capitalized.

"""


class Direction(Enum):
    NORTH = "NORTH"
    SOUTH = "SOUTH"
    WEST = "WEST"
    EAST = "EAST"

    def __deepcopy__(self, memodict={}):
        return self.value
