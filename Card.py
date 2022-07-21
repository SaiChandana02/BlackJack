class Card:
    def __init__(self,cardSymbol,suite):
        self.cardSymbol = cardSymbol
        self.suite = suite

    def getCurrentCardPoints(self):
        if self.cardSymbol=="King"or self.cardSymbol=="Queen" or self.cardSymbol=="Jack":
            return  10
        elif self.cardSymbol=="Ace":
            return 0
        else :
          return int(self.cardSymbol)
        

