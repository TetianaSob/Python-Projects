# Decorators_show_args.py

'''Write a fuction called 'show_args' which accepts a function and 
returns another function. Before invoking the function passed to it,
show_args should be responsible for printing two things: 
a tuple of the positional arguments, and a dictionaru of the keyword
arguments.'''
'''
@show_args
def do_nothing(*args, **kwargs):
    pass

do_nothing(1, 2, 3,a="hi",b="bye")

# Should print (on two lines):
# Here are the args: (1, 2, 3)
# Here are the kwargs: {"a": "hi", "b": "bye"}
'''
'''
Show Args Decorator Solution
ignoring all the boilerplate code (the stuff that goes in every decorator function, wraps,e tc.), the important logic is really just:

        print("Here are the args:", args)
        print("Here are the kwargs:", kwargs)
        return fn(*args, **kwargs)
Here's the complete code:
'''

from functools import wraps
 
def show_args(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        print("Here are the args:", args)
        print("Here are the kwargs:", kwargs)
        return fn(*args, **kwargs)
    return wrapper

# @show_args
# def do_nothing(*args, **kwargs):

# print(wrapper()) 
# print(show_args({"a": "hi", "b": "bye"}))
