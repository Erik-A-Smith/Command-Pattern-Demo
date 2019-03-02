from Classes.Command import Command

class PlayCommand(Command):
    def __init__(self,player):
        self.player = player
        
    def execute(self):
        card = self.player.play()
        print("{0} Played: \n{1}".format(self.player.name, str(card) ) )
        return card
    
    