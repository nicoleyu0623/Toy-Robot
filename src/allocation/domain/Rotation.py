# @Time : 21/7/22 1:15 pm
# @Original Author : Nicole Yu
# @File : Rotation.py
# @Project: AUTOMATION

from enum import Enum

""" Rotation class

This modules enumerate the way of rotation that robot capable of. 
All the ways of rotation are capitalized.

"""


class Rotation(Enum):
    LEFT = "LEFT"
    RIGHT = "RIGHT"

    def __deepcopy__(self, memodict={}):
        return self.value
