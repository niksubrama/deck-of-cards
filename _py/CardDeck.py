# Simulate Deck of cards with 2 operations: shuffle() and dealOneCard()
# Three Classes -  Card, Deck, Player. Player is optional.

import random

# Define combinations of suits and face values
class Card(object): 
    def __init__(self, suit, val):
        self.suit = suit
        self.value = val
        
    # To print card object as string
    def __unicode__(self):
        return self.show()
    def __str__(self):
        return self.show()
    def __repr__(self):
        return self.show()
        
    def show(self):
        if self.value == 13:  
            val = "King"
        elif self.value == 12:
            val = "Queen";
        elif self.value == 11:
            val = "Jack";
        elif self.value == 1:
            val = "Ace";
        else: 
            val = self.value; 
        return "{} of {}". format(val, self.suit)
        
class Deck(object):
    def __init__(self):
        self.cards = []
        self.build()
    
    #Show all cards in deck
    def show(self):    
        for card in self.cards:
                print card.show()
                
    #Create playing deck of 52 cards
    def build(self):
     self.cards = [] 
     #build 4 playing suits
     for suit in ['Hearts', 'Spades', 'Clubs', 'Diamonds']:
         for val in range(1, 14):
             self.cards.append(Card(suit,val))
             
    # Shuffle returns no value, it results in the cards in the deck being randomly permuted.
    def shuffle(self, num=1):
        length = len(self.cards)
        for _ in range(num):
            for i in range(length-1, 0, -1):
                r = random.randint(0, i)
                if i == r:
                    continue
                self.cards[i], self.cards[r] = self.cards[r], self.cards[i]
            
    # This function returns one card from the deck to the caller.
    def dealOneCard(self):
        try:
            return self.cards.pop()
        except:
            print "-------------"
            print "No more cards"
    
# Simulates a player drawing a card from the deck    
class PlayerOperator(object):
    def __init__(self, firstName):
        self.firstName = firstName
        self.hand = [] #array

    def draw(self, deck, num=1):
        try: 
            for _ in range(num):
                card = deck.dealOneCard() #get one card at a time from randomly shuffled deck
                if card:
                    self.hand.append(card) #append card(s)
                else:
                    #print "no more"
                    return False #no more cards to return
            return True #card was drawn successfully
        except: 
            print "There was an issue in drawing the card"
            #return False

    def showHand(self):
        print "*********************"
        print "{}'s hand: {}".format(self.firstName, self.hand)
        return self
 

# Run operations

myAppDeck = Deck() #create a deck
myAppDeck.shuffle() #shuffle it in random order
caroline = PlayerOperator("Caroline") #assign it to a player

# A call to shuffle followed by 52 calls to dealOneCard() should result in the caller being provided all 52 cards of the deck in random order. 
# If the caller then makes a 53rd call dealOneCard(), no card is dealt. 

for _ in range(53): #draw 1 card, 53 times
    caroline.draw(myAppDeck, 1) #draw one card

caroline.showHand() #show current list of drawn cards
