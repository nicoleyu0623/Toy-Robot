# @Time : 22/7/22 5:16 pm
# @Original Author : Nicole Yu
# @File : test_multi_instructions.py
# @Project: AUTOMATION


import re

instruction = "PLACE 0,0,NORTH"
first_valid_initial_position = instruction.split(" ")[1]
first_valid_initial_position_regex = re.compile(
    r"^[0-4],[0-4],[NORTH|WEST|EAST|SOUTH]*$"
)
int = first_valid_initial_position_regex.search(first_valid_initial_position)

if int:
    print("yes")
