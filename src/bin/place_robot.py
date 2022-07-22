# @Time : 21/7/22 1:21 pm
# @Original Author : Nicole Yu
# @File : place_robot.py
# @Project: AUTOMATION
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.allocation.domain.Position import Position
from src.allocation.domain.Rotation import Rotation
from src.allocation.domain.Direction import Direction
from src.allocation.domain.Instructions import Instructions
from src.allocation.domain.Robot import Robot
import re
from src.utils.log_util import LOGGER
from typing import List

""" The entrypoint module that facilitate the whole game.

The initial instruction must contains instruction "PLACE" 
along with the position and direction of the bot to start the game.
If the initial instruction is not well-formatted, then the program will log the error messages.

>> Example of the initial instruction: "PLACE 1,2,EAST"

Then the user should hit <enter> key to interact with the program, and key in the followed instructions.

After each instruction, user should hit <enter> key. 

The position, direction of the robot and user instruction will be tracked in log.
"""


def main():
    # Start to do the initialization until valid input is entered.
    robot = None

    while True:
        instruction: str = input("Please enter your instruction: \n")
        LOGGER.info(f"instruction is: {instruction}")

        # initial valid input
        if (Instructions.PLACE.value in instruction) and (robot == None):

            first_valid_initial_position: str = instruction.split(" ")[1]

            # instruction validation
            initial_position_regex = re.compile(
                r"^[0-4],[0-4],[NORTH|WEST|EAST|SOUTH]*$"
            )
            if initial_position_regex.search(first_valid_initial_position):
                LOGGER.info(f"Valid first instruction {instruction}")
                # construct robot instance with the initial valid position and direction
                first_valid_initial_position_list: List[
                    str
                ] = first_valid_initial_position.split(",")
                robot_initial_position: Position = Position(
                    int(first_valid_initial_position_list[0]),
                    int(first_valid_initial_position_list[1]),
                )
                robot_initial_direction: Direction = Direction(
                    first_valid_initial_position_list[2]
                )
                robot: Robot = Robot(robot_initial_direction, robot_initial_position)
                LOGGER.info(
                    f"Robot initialization with initial direction: {robot_initial_direction}, position: {robot.current_position.x},{robot.current_position.y} "
                )
                continue
            else:
                print(
                    f"Invalid initial position and instruction {first_valid_initial_position}."
                )
                LOGGER.error(
                    f"Invalid initial position and instruction {first_valid_initial_position}."
                )
                continue
        # unable to start due to invalid position and initialization
        elif robot == None:
            print(
                f"Invalid instruction {instruction}. Please enter a valid position and instruction to start the game."
            )
            LOGGER.error(f"Invalid instruction {instruction}")
            continue

        # robot move position
        if instruction == Instructions.MOVE.value and robot is not None:
            robot.move()
            LOGGER.info(
                f"robot moved to position: {robot.current_position.x},{robot.current_position.y},{robot.current_direction.value} with instruction {instruction}"
            )

        # robot rotation
        if (
            instruction == Instructions.LEFT.value
            or instruction == Instructions.RIGHT.value
        ):
            LOGGER.info(
                f"robot moved to position: {robot.current_position.x},{robot.current_position.y},{robot.current_direction.value} with instruction {instruction}"
            )
            robot.rotate(rotation_input=Rotation(instruction))

        # robot final position reporting
        if instruction == Instructions.REPORT.value and robot is not None:
            robot.report()
            LOGGER.info(
                f"Reporting: robot moved to position: {robot.current_position.x},{robot.current_position.y},{robot.current_direction.value} "
            )
            break


if __name__ == "__main__":
    main()
