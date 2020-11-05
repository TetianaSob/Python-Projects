#Ex-50_functions.py
''' is_polindrome'''

'''Write a function called is_palindrome. 
A Palindrome in a word, phrase, number, or other sequence of characters 
which reads the same backword or forward. This function should take in 
one parameter and returns 'True' or 'False' depending on the capitalization
so that is_palindrome('a man a plan a canal)'''

'''
is_palindrome('testing') # False
is_palindrome('tacocat') # True
is_palindrome('hannah') # True
is_palindrome('robert') # False
is_palindrome('amanaplanacanalpanama') # True
'''

def is_palindrome(string):
    return string == string[::-1]

print(is_palindrome('testing')) # False
print(is_palindrome('tacocat')) # True
print(is_palindrome('hannah')) # True
print(is_palindrome('robert')) # False

print("\n")
#############

def is_palindrome2(string):
    stripped = string.replace(" ", "")
    return stripped == stripped[::-1]

print(is_palindrome2('testing')) # False    
print(is_palindrome2('tacocat')) # True
print(is_palindrome2('hannah')) # True