# Ex-46_functions.py
'''number_compare'''

'''Write a function called number_compare. This function takes parameters (both numbers)
If the first is greater than the second, this fumction returns :First is greater.
If the second number is greater than the first, the function returns "Second is greater".
Otherwise the function returns "Numbers are equal".'''
'''
number_compare(1,1) # "Numbers are equal"
number_compare(1,0) # "First is greater"
number_compare(2,4) # "Second is greater"
'''

def number_compare(num1, num2):
    if num1 == num2:
        return "Numbers are equal"
    if num1 > num2:
        return "First is greater"
    else: 
        return "Second is greater"
    
print(number_compare(2, 5)) # Second is greater
print(number_compare(18, 5)) # First is greater
print(number_compare(1, 1)) # Numbers are equal

print("\n")
###############

def number_compare2(a,b):
    if a > b:
        return "First is greater"
    elif b > a:
        return "Second is greater"
    return "Numbers are equal"

print(number_compare2(3,4)) # Second is greater

#############
