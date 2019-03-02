class Player:
    
    def __init__(self, name, deck):
        self.name = name
        self.deck = deck
        self.hand = []
        self.score = 0

    def __str__(self):
        compiledString = "-----------Player {}-----------\n".format(self.name)
        compiledString += "Score: {}\n".format(self.score)
        return compiledString
    
    def draw(self, deck, quantity = 1):
        return self.cardsToHand(self.deck.draw(quantity))
        
    
    def shuffle(self,deck):
        return deck.shuffle()
    
    def cardsToHand(self,cards):
        if(isinstance(cards, list)):
            # Array of cards to be added
            self.hand.extend(cards)
        else:
            # Single card added
            self.hand.append(cards)
        return cards
    
    def play(self, index = 0):
        if(len(self.hand) <= index):
            raise Exception('Not enough cards in hand to play')
        card = self.hand.pop(index)
        self.score += card.value
        return card
        

