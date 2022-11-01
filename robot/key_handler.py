from robot import const as c
from robot.directions import Directions, Gears, Turn_Speeds, Drifts, LEDs
from robot import keys


"""
Process an incoming key event and update the bot's Directions accordingly.

:param key: The key event.
:param is_press: True if the user pressed the key; False if they released it.

:return: True if something changed; False if the key was already pressed or released
         and therefore nothing changed.
"""
def process_keys(key: str, is_press: bool) -> bool:
    # If the user pressed a key we don't care about tracking, ignore it
    if key not in c.KEYS:
        return False

    # If this event doesn't change anything (e.g. the user is just holding down a
    # key, don't do anything)
    if c.KEYS[key] == is_press:
        return False

    # Update the key state
    c.KEYS[key] = is_press

    determine_direction()

    if key in keys.GEAR_KEYS:
        determine_gear()
    elif key in keys.TURN_KEYS:
        determine_turn()
    elif key in keys.DRIFT_KEYS:
        determine_drift()
    elif key in keys.LED_KEYS:
        determine_led()

    return True


"""
Determine which Direction enum to use based on the keys that are currently pressed.
"""
def determine_direction():
    if c.KEYS[keys.FORWARD] and not c.KEYS[keys.BACKWARD]:
        if c.KEYS[keys.LEFT] and not c.KEYS[keys.RIGHT]:
            c.DIRECTION = Directions.FORWARD_LEFT
        elif c.KEYS[keys.RIGHT] and not c.KEYS[keys.LEFT]:
            c.DIRECTION = Directions.FORWARD_RIGHT
        else:
            c.DIRECTION = Directions.FORWARD

    elif c.KEYS[keys.BACKWARD] and not c.KEYS[keys.FORWARD]:
        if c.KEYS[keys.LEFT] and not c.KEYS[keys.RIGHT]:
            c.DIRECTION = Directions.BACKWARD_LEFT
        elif c.KEYS[keys.RIGHT] and not c.KEYS[keys.LEFT]:
            c.DIRECTION = Directions.BACKWARD_RIGHT
        else:
            c.DIRECTION = Directions.BACKWARD

    elif c.KEYS[keys.ZERO_LEFT]:
        c.DIRECTION = Directions.ZERO_LEFT

    elif c.KEYS[keys.ZERO_RIGHT]:
        c.DIRECTION = Directions.ZERO_RIGHT

    elif c.KEYS[keys.LINE_TRACK]:
        c.DIRECTION = Directions.LINE_TRACK

    else:
        c.DIRECTION = Directions.STOP


"""
Set the gear if the user changed it.
"""
def determine_gear():
    if c.KEYS[keys.FIRST_GEAR]:
        c.GEAR = Gears.FIRST
    elif c.KEYS[keys.SECOND_GEAR]:
        c.GEAR = Gears.SECOND
    elif c.KEYS[keys.THIRD_GEAR]:
        c.GEAR = Gears.THIRD
    elif c.KEYS[keys.FOURTH_GEAR]:
        c.GEAR = Gears.FOURTH
    elif c.KEYS[keys.FIFTH_GEAR]:
        c.GEAR = Gears.FIFTH


"""
Set the turn speed if the user changed it.
"""
def determine_turn():
    if c.KEYS[keys.TURN_VERY_SLOW]:
        c.TURN_SPEED = Turn_Speeds.VERY_SLOW
    elif c.KEYS[keys.TURN_SLOW]:
        c.TURN_SPEED = Turn_Speeds.SLOW
    elif c.KEYS[keys.TURN_MEDIUM]:
        c.TURN_SPEED = Turn_Speeds.MEDIUM
    elif c.KEYS[keys.TURN_FAST]:
        c.TURN_SPEED = Turn_Speeds.FAST
    elif c.KEYS[keys.TURN_VERY_FAST]:
        c.TURN_SPEED = Turn_Speeds.VERY_FAST


"""
Set the drift amount if the user changed it.
"""
def determine_drift():
    if c.KEYS[keys.DRIFT_LEFT_1]:
        c.DRIFT = Drifts.LEFT_1
    elif c.KEYS[keys.DRIFT_LEFT_2]:
        c.DRIFT = Drifts.LEFT_2
    elif c.KEYS[keys.DRIFT_LEFT_3]:
        c.DRIFT = Drifts.LEFT_3
    elif c.KEYS[keys.DRIFT_LEFT_4]:
        c.DRIFT = Drifts.LEFT_4
    elif c.KEYS[keys.DRIFT_NONE]:
        c.DRIFT = Drifts.NONE
    elif c.KEYS[keys.DRIFT_RIGHT_1]:
        c.DRIFT = Drifts.RIGHT_1
    elif c.KEYS[keys.DRIFT_RIGHT_2]:
        c.DRIFT = Drifts.RIGHT_2
    elif c.KEYS[keys.DRIFT_RIGHT_3]:
        c.DRIFT = Drifts.RIGHT_3
    elif c.KEYS[keys.DRIFT_RIGHT_4]:
        c.DRIFT = Drifts.RIGHT_4


"""
Set the led design if the user changed it.
"""
def determine_led():
    if c.KEYS[keys.LED_DESIGN_1]:
        c.LED = LEDs.DESIGN_1
    elif c.KEYS[keys.LED_DESIGN_2]:
        c.LED = LEDs.DESIGN_2
    elif c.KEYS[keys.LED_DESIGN_3]:
        c.LED = LEDs.DESIGN_3
    elif c.KEYS[keys.LED_DESIGN_4]:
        c.LED = LEDs.DESIGN_4
    elif c.KEYS[keys.LED_DESIGN_5]:
        c.LED = LEDs.DESIGN_5
    elif c.KEYS[keys.LED_OFF]:
        c.LED = LEDs.OFF