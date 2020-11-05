# Ex-79_Chicken_Coop_Exercise.py

'''Suppose we have a big ol chicken coop in our backyard of 
very productive hens. We are going to model our chickens with python. 
We want to keep track of how many eggs each individual Chicken lays,
and at the same time we want to track the total number od eggs
all hens have laid.

Create a Chicken class. Each Chicken has a species and name,
as well as an integer called eggs. eggs should always start out at 0.
'''
# Chicken Coop Exercise Solution:
# Here's my implementation of the Chicken class.  Notice the total_eggs class attribute.

class Chicken:
    total_eggs = 0
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.eggs = 0
    
    def lay_egg(self):
        self.eggs += 1
        Chicken.total_eggs += 1
        return self.eggs

print(Chicken.total_eggs)  # 0   
egg1 = Chicken("Blue", "chicken")
egg2 = Chicken("One", "chicken")     

print("\n")

print(egg1.name) # Blue
print(egg2.name) # One

print(egg1.species) # chicken
print(egg2.species) # chicken

print("\n")

egg2.name = "Sal"
print(egg2.name) # Sal

egg1.name = "Dell"
print(egg1.name) # Dell