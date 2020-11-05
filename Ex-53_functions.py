# Ex-53_functions.py

'''capitalize'''

'''Write a function called capitalize. This function accepts a string and returns
the same string with the first letter capitalized. You may want to use slices to help
you out.'''

'''
capitalize("tim") # "Tim"
capitalize("matt") # "Matt"
'''

def capitalize(string):
    return string[:1].upper() + string[1:]
    
print(capitalize("tim")) # Tim
print(capitalize("matt")) # Matt
