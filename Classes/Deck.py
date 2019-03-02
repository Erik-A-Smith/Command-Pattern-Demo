from Classes.Card import Card
from Classes.Face import Face
from Classes.Suit import Suit
import random

class Deck:
    cards = []
    
    def __init__(self):
        self.cards = self.generateDeck(Suit.asArray(),Face.asArray())
    
    def __str__(self):
        compiledString = "-----------my deck of cards-----------\n"
            
        for card in self.cards:
            compiledString += str(card) + "\n"

        return compiledString

    def generateDeck(self,suits,faces):
        deck = []
        for suit in suits:
            for face in faces:
                card = Card(suit,face,face)
                deck.append(card)
        return deck
    
    def shuffle(self):
        random.shuffle(self.cards)

    def draw(self, quantity = 1):

        if(len(self.cards) < quantity):
            raise Exception('Not enough cards in deck to draw {}'.format(quantity))

        # Single draw
        if(quantity == 1):
            return self.cards.pop(quantity)
        
        # Multi draw
        cards = []
        for index in range(quantity):
            cards.append(self.cards.pop())
        return cards
