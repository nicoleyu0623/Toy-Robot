# @Time : 22/7/22 7:43 pm
# @Original Author : Nicole Yu
# @File : test_exceptions.py
# @Project: AUTOMATION

import pytest

from src.allocation.exceptions.OutOfRangeError import PositionNotInRangeError
from src.allocation.validations.verify import verify_position
import math


def test_verify_position_exception_exceed_index():
    with pytest.raises(PositionNotInRangeError):
        verify_position(12, 12)


def test_verify_position_exception_neg_index():
    with pytest.raises(PositionNotInRangeError):
        verify_position(-1, -1)


def test_verify_position_exception_float_index():
    with pytest.raises(PositionNotInRangeError):
        verify_position(1.3, -1.3)


def test_verify_position_exception_infinity_index():
    with pytest.raises(PositionNotInRangeError):
        verify_position(math.inf, -1)
