
        
        from ast import Not
from math import gamma
from Deck import Deck
from Player import Player
class Game:
    allPlayers = []
    def __init__(self,userName1,userName2):
        self.__createPlayers(userName1,userName2)
        self.Deck = self.__createDeck()


    def __createPlayers(self,userName1,userName2):
        player1 = Player(userName1)
        player2 = Player(userName2)
        Game.allPlayers.append(player1)
        Game.allPlayers.append(player2)

    def __createDeck(self):
        return Deck()

    def resultAnalyzer(self):
        player1 = Game.allPlayers[0]
        player2 = Game.allPlayers[1]
        if player1.getPlayerPoints() == 21:
            return True,player1.getUserName()
        if player2.getPlayerPoints() == 21:
            return True,player2.getUserName()
        if player1.getPlayerPoints() > 21:
            return True,player1.getUserName()
        if player2.getPlayerPoints() > 21:
            return True,player2.getUserName()
        
        
