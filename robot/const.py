#mhfrom typing import Dict
from typing import Dict
from robot.directions import Directions, Gears, Turn_Speeds, Drifts, LEDs
from robot import keys

KEYS: Dict[str, bool] = {
    keys.FORWARD: False,
    keys.BACKWARD: False,
    keys.LEFT: False,
    keys.RIGHT: False,
    keys.ZERO_LEFT: False,
    keys.ZERO_RIGHT: False,
    keys.LINE_TRACK: False,
    keys.FIRST_GEAR: False,
    keys.SECOND_GEAR: False,
    keys.THIRD_GEAR: False,
    keys.FOURTH_GEAR: False,
    keys.FIFTH_GEAR: False,
    keys.TURN_VERY_SLOW: False,
    keys.TURN_SLOW: False,
    keys.TURN_MEDIUM: False,
    keys.TURN_FAST: False,
    keys.TURN_VERY_FAST: False,
    keys.DRIFT_LEFT_4: False,
    keys.DRIFT_LEFT_3: False,
    keys.DRIFT_LEFT_2: False,
    keys.DRIFT_LEFT_1: False,
    keys.DRIFT_NONE: False,
    keys.DRIFT_RIGHT_1: False,
    keys.DRIFT_RIGHT_2: False,
    keys.DRIFT_RIGHT_3: False,
    keys.DRIFT_RIGHT_4: False,
    keys.LED_OFF: False,
    keys.LED_DESIGN_1: False,
    keys.LED_DESIGN_2: False,
    keys.LED_DESIGN_3: False,
    keys.LED_DESIGN_4: False,
    keys.LED_DESIGN_5: False
}

DIRECTION: Directions = Directions.STOP

GEAR: Gears = Gears.THIRD

TURN_SPEED: Turn_Speeds = Turn_Speeds.MEDIUM

DRIFT: Drifts = Drifts.NONE

LED: LEDs = LEDs.OFF

EXIT = False