# @Time : 21/7/22 1:27 pm
# @Original Author : Nicole Yu
# @File : verify.py
# @Project: AUTOMATION
from src.allocation.exceptions.OutOfRangeError import PositionNotInRangeError


def verify_position(x: int, y: int) -> bool:
    """
    To verify whether robot in the 4x4 square.
    :param x: (int) robot's horizontal position
    :param y: (int) robot's vertical position
    :return: bool whether robot is in the square
    """
    is_valid: bool = (x >= 0) and (y >= 0) and (x <= 4) and (y <= 4)
    if not is_valid:
        raise PositionNotInRangeError(x, y)

    return is_valid
