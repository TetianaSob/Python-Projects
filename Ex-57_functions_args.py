# Ex-57_functions_args.py

''' *args Exercise: The Purple Test

Define a function 'contains_purple' that accepts any number of arguments.
It should return 'True' if any of the arguments are purple (all lowercase).
Otherwise, it should return 'False'. For example:'''

#contains_purple(25, "purple") # True

def contains_purple(*args):
    if "purple" in args:
        return True
    
    return False

print(contains_purple(25, "purple")) # True
print(contains_purple("green", False, 37, "blue", "hello world")) # False

print("\n")
###############

'''Remember, I don't need to write the else  part of the conditional in this case, 
because I'm returning out of the function on the line before. So the only 
way the return False  line runs is if the above line didn't run.  It's an 
implicit else.'''

def contains_purple2(*args):
    if "purple" in args: return True
    return False

print(contains_purple2("green", False, 37, "blue", "hello world")) # False