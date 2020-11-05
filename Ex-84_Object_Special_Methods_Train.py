# Ex-84_Object_Special_Methods_Train.py

'''Special Methods Train

Create a class 'Train' that has one attribute: 'num_cars' which is specified
when the train in instantiated.

There should also be two speacial/magic/dunder methods on it:

- One method that describes the train when we call 'print' on it by 
saying "x car train" where x is the number of cars (see example below)
- One method that denotes the length of the train when we call on it

Example:
a_train = Train(4)
print(a_train)
len(a_train)

You do not need to instantiate 'Train' for the tests to pass. The 
tests will try to instantiate 'Train' for you.

class Train:
    pass

'''

#Special Methods Train Solution

class Train():
    def __init__(self, num_cars):
        self.num_cars = num_cars
 
    def __repr__(self):
        return "{} car train".format(self.num_cars)
 
    def __len__(self):
        return self.num_cars

tr1 = Train('20')
print(f"{tr1} the number of cars") # 20 car train the number of cars
