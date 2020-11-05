# Ex-92_only_ints.py

'''Write a function called 'only_ints' which accepts a function and returns
another function. The function passed to it should be invoked if all of the
arguments passed to it are integers. Otherwise the inner function should 
return "Please only invoke with integers." '''

'''
@only_ints 
def add(x, y):
    return x + y
    
add(1, 2) # 3
add("1", "2") # "Please only invoke with integers."
'''

#Only Ints Decorator Exercise

from functools import wraps
 
def only_ints(fn):
    @wraps(fn)
    def inner(*args, **kwargs):
        if any([arg for arg in args if type(arg) != int]):
            return "Please only invoke with integers."
        return fn(*args, **kwargs)
    return inner

def add(x, y):
    return x + y
    
print(add(1, 2)) # 3
print(add("1", "2")) # 12
