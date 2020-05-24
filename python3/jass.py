# https://stackoverflow.com/questions/4932438/how-to-create-a-custom-string-representation-for-a-class-object
from random import shuffle
from datetime import datetime

class Card:
    def __init__(self, value):
        self.value = value
    def __repr__(self): 
        return self.value
    def beats(self, card): #TODO: do I need this or can I rely on string <> comparison?
        i = Deck.allowedValues.index(self.value, 0, len(Deck.allowedValues))
        j = Deck.allowedValues.index(card.value, 0, len(Deck.allowedValues))
        if (i > j):
            return True
        elif (i < j):
            return False
        else:
            return None

class Deck:
    allowedValues = ['06','07','08','09','10','Bu','Da','Ko','SS']
    def __init__(self):
        cards = []
        for v in self.allowedValues:
            for k in range(4):
                cards.append(Card(v))
        self.cards = cards
        shuffle(self.cards)
        
class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []
    def __repr__(self):
        return self.name + ' ' + str(self.hand)
    def sort(self):
        self.hand.sort(key=lambda x: x.value, reverse=False) #usually sorts their hand after they get their cards

class Game:
    def dealCards(self):
        handSize = int(len(self.deck.cards) / len(self.players))
        for p in self.players:
            for i in range(handSize):
                p.hand.append(self.deck.cards.pop(0))
    def play(self):
        winner = None
        while (winner is None):
            winner = self.players.pop()
            #TODO: implement game play..
        print ('winner is:', winner)
            
    def __init__(self, players, deck):
        self.players = players
        self.deck = deck
        self.dealCards()
        for p in self.players:
            p.sort()
        self.play()
    
# ... OK, then lets play...
startTime = datetime.now()
for i in range(1):
    newGame = Game([Player('Mommy'), Player('Daddy'), Player('Luke')], Deck())
    print(newGame.players)
    
print(datetime.now() - startTime, 'expired') 
