# @Time : 22/7/22 7:55 pm
# @Original Author : Nicole Yu
# @File : test_validations.py
# @Project: AUTOMATION
import pytest
from src.allocation.validations.verify import verify_position

import pytest


@pytest.mark.parametrize(
    "maybe_valid_x, maybe_valid_y, expected_result",
    [
        (3, 3, True),
        (3, 1, True),
        (0, 1, True),
        (0, 0, True),
        (4, 4, True),
    ],
)
def test_verify_position(maybe_valid_x, maybe_valid_y, expected_result):
    assert verify_position(maybe_valid_x, maybe_valid_y) == expected_result
