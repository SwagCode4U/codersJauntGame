from enum import Enum, auto

class Enemy(Enum):
    ZOMBIE = auto()
    ROBOT = auto()

class Weapon(Enum):
    SWORD = auto()
    GUN = auto()

class Topic(Enum):
    OOPS = auto()
    REGEX = auto()
    EXCEPTIONS = auto()
    FILE_HANDLING = auto()
