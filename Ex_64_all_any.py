# Ex_64_all_any.py

# Any/All Exercise

'''Implement a function 'is_all_strings' that accepts a single iterable 
and returns True if it contains ONLY strings. Otherwise, it should return false.'''

''' is_a;;_strings(['a', 'b', 'c'])'''
''' is_a;;_strings([2, 'a', 'b', 'c'])'''

# Implement your is_all_strings function below:
def is_all_strings(lst):
    return all(type(l) == str for l in lst)
    
print(is_all_strings(['a', 'b', 'c'])) # True

print("\n")
''' is_all_strings solution 
Using a Generator Expression

I start by defining is_all_strings, which accepts a parameter called lst
I call the built-in function all, passing in a generator expression that checks 
if the type of each item in the list is a str.'''

def is_all_strings2(lst):
    return all(type(l) == str for l in lst)

print(is_all_strings2(['a', 'b', 'c'])) # True   

print("\n")
''' Using a List Comprehension

You can do the same thing, using a list comprehension instead of 
a generator expression: (just add list brackets around it) '''

def is_all_strings3(lst):
    return all([type(l) == str for l in lst])

print(is_all_strings3(['a', 'b', 'c'])) # True 