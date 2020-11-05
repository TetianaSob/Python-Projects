# Decorators3_Syntax2.py

def shout(fn):
    def wrapper(name):
        return fn(name).upper()
    return wrapper

@shout
def greet(name):
    return f"Hi, I'm {name}."

print(greet("todd"))  # HI, I'M TODD.

print("\n")
###########

def shout(fn):
    def wrapper(*args, **kwargs):  # toaccept mumtiple arguments
        return fn(*args, **kwargs).upper()
    return wrapper

@shout
def greet(name):
    return f"Hi, I'm {name}."

@shout
def order(main, side):
    return f"Hi, I'd like the {main}, with a side of {side}, please."

@shout
def lol():
    return "lol"

print(greet("todd"))  # HI, I'M TODD.
print(order(side="burger", main="fries"))  # HI, I'D LIKE THE BURGER, WITH A SIDE OF FRIES, PLEASE.
print(lol()) # LOL 
