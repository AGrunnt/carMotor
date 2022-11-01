from robot.Motor import *
from robot import const as c
from robot.directions import Directions, Gears, Turn_Speeds, Drifts
from robot.Line_Tracking import Line_Tracking

import sys, time
from typing import List, Tuple


"""
This is the max speed setting for the robot, used in gear 5.
"""
MAX_SPEED = 4096

"""
This is the percentage that one side's motors are decreased to account for drift.
If drift is set to LEFT_1 and this is 0.05, the motors on the right side are multiplied
by 0.95. For LEFT_2, they're multiplied by 0.9; for LEFT_3, by 0.85; etc.
"""
DRIFT_INCREMENT = 0.15


"""
Initialize the Robot. This should be run in its own distinct thread.
"""
def initialize():
    global my_Motor, infrared


    print('Initializing robot')

    my_Motor = Motor()
    infrared = Line_Tracking()

    listener()


"""
Starts an inifinite loop checking the const.py file for changes. This will control
the robot movement.
"""
def listener():
    while True:
        # Check the const file for changes
        if c.EXIT:
            sys.exit()

        uniform_speed, turn_speed_opt = get_speeds()
        wheel_speeds = turn(uniform_speed, turn_speed_opt)
        wheel_speeds = adjust_drift(wheel_speeds)
        move(wheel_speeds)


"""
Calculate speeds based on Gear and Turn_Speed settings.

Returns a list of integers (the default speed for each wheel based on the gear),
and a float representing the turn_speed_opt.

turn_speed_opt is a measure of how sharply the bot makes turns.
"""
def get_speeds() -> Tuple[List[int], float]:
    # If a change speed key is click, change speed to that amount

    if c.GEAR==Gears.FIRST:
        new_speed = MAX_SPEED * 0.15
    elif c.GEAR==Gears.SECOND:
        new_speed = MAX_SPEED * 0.2
    elif c.GEAR==Gears.THIRD:
        new_speed = MAX_SPEED * 0.50
    elif c.GEAR==Gears.FOURTH:
        new_speed = MAX_SPEED * 0.70
    elif c.GEAR==Gears.FIFTH:
        new_speed = MAX_SPEED * 1.0

    new_speed_list = [int(new_speed) for i in range(4)]

    # Potentially scale these these so that VERY_FAST has a negative turn_speed_opt
    if c.TURN_SPEED == Turn_Speeds.VERY_FAST:
        turn_speed_opt = -0.6
    elif c.TURN_SPEED == Turn_Speeds.FAST:
        turn_speed_opt = -0.3
    elif c.TURN_SPEED == Turn_Speeds.MEDIUM:
        turn_speed_opt = 0
    elif c.TURN_SPEED == Turn_Speeds.SLOW:
        turn_speed_opt = 0.2
    elif c.TURN_SPEED == Turn_Speeds.VERY_SLOW:
        turn_speed_opt = 0.5

    return new_speed_list, turn_speed_opt


"""
Calculate the actual speeds for each wheel based on the given uniform_speed (determined
by the gear) and the amount of turning.
"""
def turn(uniform_speed: List[int], turn_speed_opt: float) -> List[int]:
    global infrared

    if c.DIRECTION == Directions.FORWARD_LEFT:
        """
        uniform_speed[0] = uniform_speed[0] * turn_speed_opt
        uniform_speed[1] = uniform_speed[1] * turn_speed_opt
        #uniform_speed[2] = uniform_speed[2] * 1
        #uniform_speed[3] = uniform_speed[3] * 1
        """

        uniform_speed[0] = 0
        uniform_speed[1] = MAX_SPEED * turn_speed_opt
        uniform_speed[2] = MAX_SPEED * 1
        uniform_speed[3] = MAX_SPEED * 1

    elif c.DIRECTION == Directions.FORWARD_RIGHT:
        """
        #uniform_speed[0] = uniform_speed[0] * 1
        #uniform_speed[1] = uniform_speed[1] * 1
        uniform_speed[2] = uniform_speed[2] * turn_speed_opt
        uniform_speed[3] = uniform_speed[3] * turn_speed_opt
        """

        uniform_speed[0] = MAX_SPEED * 1
        uniform_speed[1] = MAX_SPEED * 1
        uniform_speed[2] = 0
        uniform_speed[3] = MAX_SPEED * turn_speed_opt

    elif c.DIRECTION == Directions.BACKWARD_LEFT:
        """
        uniform_speed[0] = uniform_speed[0] * -1 * turn_speed_opt
        uniform_speed[1] = uniform_speed[1] * -1 * turn_speed_opt
        uniform_speed[2] = uniform_speed[2] * -1
        uniform_speed[3] = uniform_speed[3] * -1
        """

        uniform_speed[0] = -MAX_SPEED * turn_speed_opt
        uniform_speed[1] = 0
        uniform_speed[2] = -MAX_SPEED * 1
        uniform_speed[3] = -MAX_SPEED * 1

    elif c.DIRECTION == Directions.BACKWARD_RIGHT:
        """
        uniform_speed[0] = uniform_speed[0] * -1
        uniform_speed[1] = uniform_speed[1] * -1
        uniform_speed[2] = uniform_speed[2] * -1 * turn_speed_opt
        uniform_speed[3] = uniform_speed[3] * -1 * turn_speed_opt
        """

        uniform_speed[0] = MAX_SPEED * -1
        uniform_speed[1] = MAX_SPEED * -1
        uniform_speed[2] = MAX_SPEED * turn_speed_opt * -1
        uniform_speed[3] = 0

    elif c.DIRECTION == Directions.BACKWARD:
        return [-1 * speed for speed in uniform_speed]

    elif c.DIRECTION == Directions.ZERO_LEFT:
        # First could be 0
        return [
            -1 * uniform_speed[0], -1 * uniform_speed[1],
            uniform_speed[2], uniform_speed[3]
        ]

    elif c.DIRECTION == Directions.ZERO_RIGHT:
        # Third could be 0
        return [
            uniform_speed[0], uniform_speed[1],
            -1 * uniform_speed[2], -1 * uniform_speed[3]
        ]

    elif c.DIRECTION == Directions.LINE_TRACK:
        # This function will pause execution until c.DIRECTION is no longer
        # Directions.LINE_TRACK.
        infrared.run()

    elif c.DIRECTION == Directions.STOP:
        return [0, 0, 0, 0]

    return [int(s) for s in uniform_speed]


"""
Adjust the wheel speeds based on the drift setting. This only affects
forward, left, right, and backward movements.
"""
def adjust_drift(wheel_speeds: List[int]) -> List[int]:
    if (c.DIRECTION == Directions.FORWARD or
        c.DIRECTION == Directions.FORWARD_LEFT or
        c.DIRECTION == Directions.FORWARD_RIGHT or
        c.DIRECTION == Directions.BACKWARD):

        if c.DRIFT == Drifts.NONE:
            return wheel_speeds
        elif c.DRIFT == Drifts.RIGHT_1:
            wheel_speeds[0] = int(wheel_speeds[0] * (1 - DRIFT_INCREMENT))
            wheel_speeds[1] = int(wheel_speeds[1] * (1 - DRIFT_INCREMENT))
        elif c.DRIFT == Drifts.RIGHT_2:
            wheel_speeds[0] = int(wheel_speeds[0] * (1 - 2 * DRIFT_INCREMENT))
            wheel_speeds[1] = int(wheel_speeds[1] * (1 - 2 * DRIFT_INCREMENT))
        elif c.DRIFT == Drifts.RIGHT_3:
            wheel_speeds[0] = int(wheel_speeds[0] * (1 - 3 * DRIFT_INCREMENT))
            wheel_speeds[1] = int(wheel_speeds[1] * (1 - 3 * DRIFT_INCREMENT))
        elif c.DRIFT == Drifts.RIGHT_4:
            wheel_speeds[0] = int(wheel_speeds[0] * (1 - 4 * DRIFT_INCREMENT))
            wheel_speeds[1] = int(wheel_speeds[1] * (1 - 4 * DRIFT_INCREMENT))
        elif c.DRIFT == Drifts.LEFT_1:
            wheel_speeds[2] = int(wheel_speeds[2] * (1 - DRIFT_INCREMENT))
            wheel_speeds[3] = int(wheel_speeds[3] * (1 - DRIFT_INCREMENT))
        elif c.DRIFT == Drifts.LEFT_2:
            wheel_speeds[2] = int(wheel_speeds[2] * (1 - 2 * DRIFT_INCREMENT))
            wheel_speeds[3] = int(wheel_speeds[3] * (1 - 2 * DRIFT_INCREMENT))
        elif c.DRIFT == Drifts.LEFT_3:
            wheel_speeds[2] = int(wheel_speeds[2] * (1 - 3 * DRIFT_INCREMENT))
            wheel_speeds[3] = int(wheel_speeds[3] * (1 - 3 * DRIFT_INCREMENT))
        elif c.DRIFT == Drifts.LEFT_4:
            wheel_speeds[2] = int(wheel_speeds[2] * (1 - 4 * DRIFT_INCREMENT))
            wheel_speeds[3] = int(wheel_speeds[3] * (1 - 4 * DRIFT_INCREMENT))

    return wheel_speeds


"""
Take a list of speeds for each wheel and apply them to the robot.
"""
def move(speed_list: List[int]) -> None:
    global my_Motor

    my_Motor.setMotorModel(
        speed_list[0],
        speed_list[1],
        speed_list[2],
        speed_list[3]
    )
