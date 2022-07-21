from Card import Card
import random
class Deck:
    suites = ["Hearts","Diamonds","Spade","Club"]
    cards = ["Ace","2","3","4","5","6","7","8","9","King","Queen","Jack"]
    def __init__(self):
        self.allCards = []
        for suite in Deck.suites:
            for c in Deck.cards:
                self.allCards.append(Card(c,suite))

    def drawCard(self):
         randomCard = random.choice(self.allCards)
         self.allCards.remove(randomCard)
         return randomCard





