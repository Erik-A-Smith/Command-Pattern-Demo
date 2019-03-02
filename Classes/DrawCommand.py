from Classes.Command import Command

class DrawCommand(Command):
    def __init__(self,player,deck, quantity = 1):
        self.player = player
        self.deck = deck
        self.quantity = quantity
    
    def execute(self):
        card = self.player.draw(self.deck,self.quantity)
        print("{0} Drew a card: \n{1}".format(self.player.name, str(card) ) )
        return card
    
    