# @Time : 22/7/22 4:52 pm
# @Original Author : Nicole Yu
# @File : Instructions.py
# @Project: AUTOMATION
from enum import Enum

""" Instruction class

This modules enumerate the instructions that user could input, 
in order to give instruction to the robot.
All the instruction are capitalized.

> Example:
Please enter your instruction: 
<PLACE> 0,0,NORTH

"""


class Instructions(Enum):
    PLACE = "PLACE"
    REPORT = "REPORT"
    MOVE = "MOVE"
    LEFT = "LEFT"
    RIGHT = "RIGHT"

    def __deepcopy__(self, memodict={}):
        return self.value
