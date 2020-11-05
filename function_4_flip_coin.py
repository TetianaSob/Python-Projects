# function_4_flip_coin.py

from random import random

def flip_coin():
    #generate random number 0-1
    r = random()
    if r > 0.5:
        return "Heads"
    else:
        return "Tails"

print(flip_coin()) # Heads # Tails

print("\n")
##########

def flip_coin():
    #generate random number 0-1
    if random() > 0.5:
        return "Heads"
    else:
        return "Tails"

print(flip_coin()) # Heads # Tails