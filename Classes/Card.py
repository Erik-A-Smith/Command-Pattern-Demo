from enum import Enum

# Main card class
class Card:
    def __init__(self,suit,face, value):
        self.suit = suit
        self.face = face
        self.value = value
    
    def __str__(self):
        compiledString = "---- Card ----\n"
        compiledString += "|Suit: {} \n".format(self.suit)
        compiledString += "|Face: {} \n".format(self.face)
        compiledString += "|Value: {} \n".format(self.value)
        compiledString += "--------------"
        compiledString += "\n"
        return compiledString



    

