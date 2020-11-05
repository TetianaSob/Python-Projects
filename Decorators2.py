# Decorators2.py

''' Decorators are functions
Decorators wrap other functions and enhance their behavior
Decorators are examples of higher order functions
Decorators have their own syntax, using '@'(syntactic sugar) '''

def be_polite(fn): 
    def wrapper():  # wrapingt the functition
        print("What a pleasure to meet you!")
        fn()    # pass the secont function here
        print("Have a great day!")
    return wrapper

def greet():                                            
    print("My name is Colt.")

def rage():
    print("I hate you!")

greet = be_polite(greet)
print(greet())
# What a pleasure to meet you!
# My name is Colt.
# Have a great day!
# None
print("\n")

rage = be_polite(rage)
print(rage())
# What a pleasure to meet you!
# I hate you!
# Have a great day!
# None

