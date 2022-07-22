# @Time : 22/7/22 7:43 pm
# @Original Author : Nicole Yu
# @File : test_exceptions.py
# @Project: AUTOMATION

import pytest

from src.allocation.exceptions.OutOfRangeError import PositionNotInRangeError
from src.allocation.validations.verify import verify_position


def test_verify_position_exception():
    with pytest.raises(PositionNotInRangeError):
        verify_position(12, 12)
