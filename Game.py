
        
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
        
        if player1.getPlayerCurrentChoice()==player2.getPlayerCurrentChoice()=="skip":
            if player1.getPlayerPoints()==player2.getPlayerPoints():
                return True,"it's a Draw!!"

            return (True,player1.getUserName()) if player1.getPlayerPoints()>player2.getPlayerPoints() else (True,player2.getUserName())
        return False,""
        

    def startGame(self):
        currentPlayer = 0
        player1 = Game.allPlayers[0]
        player2 = Game.allPlayers[1]
        print("The Two choice are Skip and Draw!")
        flag,status = self.resultAnalyzer()
        while(flag==False):
            inputChoice = input("Enter the "+str(currentPlayer)+" choice ")
            if currentPlayer==0:
                player1.currentChoice = inputChoice
                if player1.getPlayerCurrentChoice()=="Skip":
                    pass
                elif player1.getPlayerCurrentChoice()=="Draw":
                    player1.selectCard(Deck)
                else:
                    print("invalid choice!!")
            else :
                player2.currentChoice = inputChoice
                if player2.getPlayerCurrentChoice()=="Skip":
                    pass
                elif player2.getPlayerCurrentChoice()=="Draw":
                    player2.selectCard(Deck)
                else:
                    print("invalid choice!!")

            currentPlayer = int(not currentPlayer)
        print(status)
                
            


if __name__=="__main__":
    newGame = Game("s","k")
    newGame.startGame()