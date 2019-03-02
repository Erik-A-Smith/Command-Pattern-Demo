#!/usr/bin/env python3

from Classes.Deck import Deck
from Classes.Player import Player
from Classes.DrawCommand import DrawCommand
from Classes.ShuffleCommand import ShuffleCommand
from Classes.PlayCommand import PlayCommand
from Classes.CommandManager import CommandManager
import random

##
# functions
#

def nextPlayer(player,players):
    currIndex = players.index(player)
    nextIndex = (currIndex + 1) % len(players)
    return players[nextIndex]

def randomPlayer(players):
    index = random.randint(0,len(players)-1)
    return players[index]

def winner():
    if len(p1.deck.cards) <= 0:
        return p2
    if len(p2.deck.cards) <= 0 :
        return p1
    if(turnsToPlay == turnsPlayed):
        return p1 if p1.score > p2.score else p2
    return False

##
# Variable declaration
#

turnsToPlay = 10 # both players included (E.G 2 players each with 5 turns. turnsToPlay => 10)

commandManager = CommandManager() # handle execution and tracking of commands
d1 = Deck()
d2 = Deck()
p1 = Player("Joe", d1)
p2 = Player("George", d2)
players = [p1,p2]
playerTurn = randomPlayer(players)
turnsPlayed = 0

##
# Command declaration
#

# Shuffle commands
p1shuffle = ShuffleCommand(p1,d1)
p2shuffle = ShuffleCommand(p2,d2)

##
# Game Logic
#  

print("=========================================\n               Game Start \n=========================================\n" )
# Both player shuffle their decks
commandManager.run(p1shuffle)
commandManager.run(p2shuffle)

# Game loop
while not winner():
    turnsPlayed += 1
    print("########################\n#      Turn {}\n########################".format(turnsPlayed) )
    drawCommand = DrawCommand(playerTurn,playerTurn.deck)
    playCommand = PlayCommand(playerTurn)
    commandManager.run(drawCommand)
    commandManager.run(playCommand)
    playerTurn = nextPlayer(playerTurn,players)
    print("Players after turn {}:".format(turnsPlayed))
    print(p1)
    print(p2)

print("Player \"{}\" won!".format(winner().name))

