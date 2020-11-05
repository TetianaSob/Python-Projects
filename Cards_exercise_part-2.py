import random
from random import shuffle

# Cards_exercise_part-2.py

'''
Deck of Cards Exercise Introduction Text

OOP Exercise
Introduction

Your goal in this exercise is to implement two classes, Card  and Deck .

Specifications

Card 

Each instance of Card  should have a suit ("Hearts", "Diamonds", "Clubs", or "Spades").
Each instance of Card  should have a value ("A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K").
Card 's __repr__  method should return the card's value and suit (e.g. "A of Clubs", "J of Diamonds", etc.)
Deck 

Each instance of Deck  should have a cards attribute with all 52 possible instances of Card .
Deck  should have an instance method called count  which returns a count of how many cards remain in the deck.
Deck 's __repr__  method should return information on how many cards are in the deck (e.g. "Deck of 52 cards", "Deck of 12 cards", etc.)
Deck  should have an instance method called _deal  which accepts a number and removes at most that many cards from the deck 
(it may need to remove fewer if you request more cards than are currently in the deck!). If there are no cards left, this method should return 
a ValueError  with the message "All cards have been dealt".
Deck  should have an instance method called shuffle  which will shuffle a full deck of cards. If there are cards missing from the deck, 
this method should return a ValueError  with the message "Only full decks can be shuffled".  shuffle should return the shuffled deck.
Deck  should have an instance method called deal_card  which uses the _deal  method to deal a single card from the deck and return that single card.
Deck  should have an instance method called deal_hand  which accepts a number and uses the _deal  method to deal a list of cards from 
the deck and return that list of cards.
'''

class Card:
    def __init__(self, value, suit):
        self.value = value 
        self.suit = suit

    def __repr__(self):              
        #return "{} of {}".format(self.value, self.suit)
        return f"{self.value} of {self.suit}"

c = Card("A", "Hearts")
c2 = Card("10", "Diamonds")
c3 = Card("K", "Spades")

print(c, c2, c3) # A of Hearts 10 of Diamonds K of Spades

 ######### v-1

# class Deck:
#     def __init__(self):
#         suits = ["Hearts", "Dimonds", "Clubs", "Spades"]
#         values = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
#         self.cards = []
#         for suit in suits:
#             for value in values:
#                 print(Card(value, suit)) # to go through the list of cards

# Deck()

#v-2

class Deck:
    def __init__(self):
        suits = ["Hearts", "Dimonds", "Clubs", "Spades"]
        values = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        self.cards = [Card(value, suit) for suit in suits for value in values]
            #print(self.cards) # to go through the list of cards 

    def __repr__(self):    # Deck 's __repr__  method should return information on how many cards are in the deck (e.g. "Deck of 52 cards", "Deck of 12 cards", etc.)
        return f"Deck of {self.count()} cards"

    def _iter__(self):
        return iter(self.cards)

    def count(self):  # Deck  should have an instance method called count  which returns a count of how many cards remain in the deck.
        return len(self.cards)

    def _deal(self, num):  # Deck  should have an instance method called _deal  which accepts a number and removes at most that many cards from the deck (it may need to remove fewer if you request more cards than are currently in the deck!). If there are no cards left, this method should return a ValueError  with the message "All cards have been dealt".
        count = self.count()
        actual = min([count, num])
        if count == 0:
            raise ValueError("All cards have been dealt")
        cards = self.cards[-actual:]
        self.cards = self.cards[:-actual]
        return cards

    def deal_card(self):     # Deck  should have an instance method called deal_card  which uses the _deal  method to deal a single card from the deck and return that single card.
        return self._deal(1)[0]

    def _deal_hand(self, hand_size):   #Deck  should have an instance method called deal_hand  which accepts a number and uses the _deal  method to deal a list of cards from the deck and return that list of cards.
        return self._deal(hand_size)

    def shuffle(self):
        if self.count() < 52:
            raise ValueError("Only full decks can be suffled")
        shuffle(self.cards)
        return self

d = Deck()
# testing the shuffle method
d.shuffle()
#print(d.cards)

# to test
card = d.deal_card()
print(card)
#hand = d.deal_hand(4)
#print(hand)

card2 = d.deal_card()
print(card2)

 
# 9 of Dimonds
# 3 of Dimonds

print("\n")
print(d._deal(5)) # [J of Spades, Q of Spades, K of Spades]

print("\n")

print(d.count()) # 52

print("\n")

print(d.cards.pop()) # K of Spades
print(d.cards.pop()) # Q of Spades

print(d.count()) #50

 ######### v-1

# A of Hearts
# 2 of Hearts
# 3 of Hearts
# 4 of Hearts
# 5 of Hearts
# 6 of Hearts
# 7 of Hearts
# 8 of Hearts
# 9 of Hearts
# 10 of Hearts
# J of Hearts
# Q of Hearts
# K of Hearts
# A of Dimonds
# 2 of Dimonds
# 3 of Dimonds
# 4 of Dimonds
# 5 of Dimonds
# 6 of Dimonds
# 7 of Dimonds
# 8 of Dimonds
# 9 of Dimonds
# 10 of Dimonds
# J of Dimonds
# Q of Dimonds
# K of Dimonds
# A of Clubs
# 2 of Clubs
# 3 of Clubs
# 4 of Clubs
# 5 of Clubs
# 6 of Clubs
# 7 of Clubs
# 8 of Clubs
# 9 of Clubs
# 10 of Clubs
# J of Clubs
# Q of Clubs
# K of Clubs
# A of Spades
# 2 of Spades
# 3 of Spades
# 4 of Spades
# 5 of Spades
# 6 of Spades
# 7 of Spades
# 8 of Spades
# 9 of Spades
# 10 of Spades
# J of Spades
# Q of Spades
# K of Spades

 ######### v-2
# [A of Hearts, 2 of Hearts, 3 of Hearts, 4 of Hearts, 5 of Hearts, 6 of Hearts, 
# 7 of Hearts, 8 of Hearts, 9 of Hearts, 10 of Hearts, J of Hearts, Q of Hearts, 
# K of Hearts]
# [A of Hearts, 2 of Hearts, 3 of Hearts, 4 of Hearts, 5 of Hearts, 6 of Hearts, 
# 7 of Hearts, 8 of Hearts, 9 of Hearts, 10 of Hearts, J of Hearts, Q of Hearts, 
# K of Hearts, A of Dimonds, 2 of Dimonds, 3 of Dimonds, 4 of Dimonds, 5 of Dimonds, 
# 6 of Dimonds, 7 of Dimonds, 8 of Dimonds, 9 of Dimonds, 10 of Dimonds, J of Dimonds, 
# Q of Dimonds, K of Dimonds]
# [A of Hearts, 2 of Hearts, 3 of Hearts, 4 of Hearts, 5 of Hearts, 6 of Hearts, 
# 7 of Hearts, 8 of Hearts, 9 of Hearts, 10 of Hearts, J of Hearts, Q of Hearts, 
# K of Hearts, A of Dimonds, 2 of Dimonds, 3 of Dimonds, 4 of Dimonds, 5 of Dimonds, 
# 6 of Dimonds, 7 of Dimonds, 8 of Dimonds, 9 of Dimonds, 10 of Dimonds, J of Dimonds, 
# Q of Dimonds, K of Dimonds, A of Clubs, 2 of Clubs, 3 of Clubs, 4 of Clubs, 5 of Clubs, 
# 6 of Clubs, 7 of Clubs, 8 of Clubs, 9 of Clubs, 10 of Clubs, J of Clubs, Q of Clubs, 
# K of Clubs]
# [A of Hearts, 2 of Hearts, 3 of Hearts, 4 of Hearts, 5 of Hearts, 6 of Hearts, 7 of Hearts, 
# 8 of Hearts, 9 of Hearts, 10 of Hearts, J of Hearts, Q of Hearts, K of Hearts, A of Dimonds, 
# 2 of Dimonds, 3 of Dimonds, 4 of Dimonds, 5 of Dimonds, 6 of Dimonds, 7 of Dimonds, 
# 8 of Dimonds, 9 of Dimonds, 10 of Dimonds, J of Dimonds, Q of Dimonds, K of Dimonds, 
# A of Clubs, 2 of Clubs, 3 of Clubs, 4 of Clubs, 5 of Clubs, 6 of Clubs, 7 of Clubs, 
# 8 of Clubs, 9 of Clubs, 10 of Clubs, J of Clubs, Q of Clubs, K of Clubs, A of Spades, 
# 2 of Spades, 3 of Spades, 4 of Spades, 5 of Spades, 6 of Spades, 7 of Spades, 8 of Spades, 
# 9 of Spades, 10 of Spades, J of Spades, Q of Spades, K of Spades]