# Ex-48_functions.py
'''multiple_letter_count'''

'''Write a function called multiple_letter_count. This function takes in one parameter (a string) 
and returns a dictionary with the keys being the letters and the vslues being the count of the letter.

Hint: use a dictionary comprehension and count()'''

'''
multiple_letter_count("awesome") # {'a': 1, 'e': 2, 'm': 1, 'o': 1, 's': 1, 'w': 1}
'''

# flesh out multiple_letter count:
#I used a dictionary comprehension. For each letter in the input string, I make 
# the key the letter itself ("a" for example), and the corresponding value is 
# the result of running count() of that letter in the string.

def multiple_letter_count(string):
    return {letter: string.count(letter) for letter in string}

print(multiple_letter_count("awesome")) 
# {'a': 1, 'w': 1, 'e': 2, 's': 1, 'o': 1, 'm': 1}