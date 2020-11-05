# Ex-90_double_return.py

'''Write a function called 'double_return' which accepts a function and returns
another function. double_return should decorate a function by returning two
copies of the inner function's value inside of the list. '''

'''
@double_return 
def add(x, y):
    return x + y
    
add(1, 2) # [3, 3]

@double_return
def greet(name):
    return "Hi, I'm " + name

greet("Colt") # ["Hi, I'm Colt", "Hi, I'm Colt"]
'''
'''
Double Return Decorator
Most of this function is decorator boilerplate...
'''
'''
from functools import wraps
 
def double_return(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        #logic goes in here...
    return wrapper
'''
#This wrapper function simply runs the function, and returns a list containing the result twice:

from functools import wraps
 
def double_return(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        val = fn(*args, **kwargs)
        return [val, val]
    return wrapper

@double_return ### decorator 1 with function 'add'
def add(x, y):
    return x + y
    
print(add(1, 2)) # [3, 3]    

@double_return  ### decorator 2 with function 'greet'
def greet(name):
    return "Hi, I'm " + name

print(greet("Colt")) # ["Hi, I'm Colt", "Hi, I'm Colt"]