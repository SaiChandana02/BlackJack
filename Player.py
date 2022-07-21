class Player:
    def __init__(self,userName):
        self.userName = userName
        self.points = 0
        self.currentChoice = ""
    
    def getPlayerPoints(self):
        return self.points

    def getPlayerCurrentChoice(self):
        return self.currentChoice

    def selectCard(self,deck):
        card = deck.drawCard()
        cardPoint = card.getCurrentCardPoints()
        if card.cardSymbol=="Ace":
            cardPoint = self.chooseAcePoints()
        self.updatePoints(cardPoint)
        return True

    def chooseAcePoints(self):
        return 1 if self.points+11>21 else 11
        
    def updatePoints(self,point):
        self.points+=point
        return True
         
    def getUserName(self):
        return self.userName