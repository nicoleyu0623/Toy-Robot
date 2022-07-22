# @Time : 21/7/22 2:08 pm
# @Original Author : Nicole Yu
# @File : OutOfRangeError.py
# @Project: AUTOMATION


class PositionNotInRangeError(Exception):
    """Exception raised for errors in the robot position

    Attributes:
        position x: horizontal position
        position y: vertical position
        message: explanation of the error
    """

    def __init__(
        self, position_x, position_y, message="Position is not in (4,4) range"
    ):
        self.position_x = position_x
        self.position_y = position_y
        self.message = message
        super().__init__(self.message)
