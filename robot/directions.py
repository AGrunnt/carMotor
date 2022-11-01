from enum import Enum


class Directions(Enum):
    STOP = 0,
    FORWARD = 1,
    BACKWARD = 2,
    FORWARD_LEFT = 3,
    BACKWARD_LEFT = 4,
    ZERO_LEFT = 5,
    FORWARD_RIGHT = 6,
    BACKWARD_RIGHT = 7,
    ZERO_RIGHT = 8,
    LINE_TRACK = 9


class Gears(Enum):
    FIRST = 0,
    SECOND = 1,
    THIRD = 2,
    FOURTH = 3,
    FIFTH = 4


class Turn_Speeds(Enum):
    VERY_SLOW = 0,
    SLOW = 1,
    MEDIUM = 2,
    FAST = 3,
    VERY_FAST = 4


class Drifts(Enum):
    LEFT_1 = 0,
    LEFT_2 = 1,
    LEFT_3 = 2,
    LEFT_4 = 3,
    NONE = 4,
    RIGHT_1 = 5,
    RIGHT_2 = 6,
    RIGHT_3 = 7,
    RIGHT_4 = 8


class LEDs(Enum):
    OFF = 0,
    DESIGN_1 = 1,
    DESIGN_2 = 2,
    DESIGN_3 = 3,
    DESIGN_4 = 4,
    DESIGN_5 = 5