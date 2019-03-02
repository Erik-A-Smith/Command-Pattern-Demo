from enum import Enum

# Helper enum for card class
class Suit(Enum):
    SPADE = 0
    DIAMOND = 1
    CLUB = 2
    HEART = 3

    @staticmethod
    def asArray():
        return [e.value for e in Suit]
