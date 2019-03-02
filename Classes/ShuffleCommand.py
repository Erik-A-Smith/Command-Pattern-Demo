from Classes.Command import Command

class ShuffleCommand(Command):
    def __init__(self,player,deck, quantity = 1):
        self.player = player
        self.deck = deck
    
    def execute(self):
        print("{} shuffled a deck\n".format(self.player.name))
        return self.player.shuffle(self.deck)
    
    