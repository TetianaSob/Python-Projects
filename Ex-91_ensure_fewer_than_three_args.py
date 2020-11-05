# Ex-91_ensure_fewer_than_three_args.py

'''Write a function called 'ensure_fewer_than_three_args' which accepts
a fucntion and returns another function. The function passed to it should 
only be involed if there are fewer than three positional arguments passed
to it. Otherwise, the inner function should return "Too many arguments!"'''

'''
@ensure_fewer_than_three_args
def add_all(*nums):
    return sum(nums)

add_all() # 0
add_all(1) # 1
add_all(1,2) # 3
add_all(1,2,3) # "Too many arguments!"
add_all(1,2,3,4,5,6) # "Too many arguments!"
'''

#Ensure Fewer Than Three Args Decorator Solution

from functools import wraps
 
def ensure_fewer_than_three_args(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        if len(args) < 3:
            return fn(*args, **kwargs)
        return "Too many arguments!"
    return wrapper

@ensure_fewer_than_three_args
def add_all(*nums):
    return sum(nums)

print(add_all()) # 0
print(add_all(1)) # 1
print(add_all(1,2)) # 3
print(add_all(1,2,3)) # "Too many arguments!"
print(add_all(1,2,3,4,5,6)) # "Too many arguments!"