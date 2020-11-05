# Decorators_Pattern.py
from functools import wraps
'''
def my_decorator(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        #do some stuff with fn(*args, **kwargs)
        pass
    return wrapper
'''

def log_function_data(fn):
    def wrapper(*args, **kwargs):
        print(f"you are about to call {fn.__name__}")
        print(f"Here'a the documentation: {fn.__doc__}")
        return fn(*args, **kwargs)
    return wrapper 

@log_function_data
def add(x, y):
    return x + y

print(add(10, 30)) 

# you are about to call add
# Here'a the documentation: None
# 40
print(add.__doc__) # None
print(add.__name__) # wrapper
#print(add) # wrappers