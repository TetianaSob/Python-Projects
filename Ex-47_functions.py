# Ex-47_functions.py
'''single_letter_count'''

'''Write a function called single_letter_count, This function takes in two paramters
(two strings). The first should be a word and the second should be a letter. 
The function returns the number of times that letter appears in word.
The function should be case insensitive(does not matter if the input is lowerscase
or uppercase). If thr letter is not found in the word, the function should return 0.'''
'''

single_letter_count("Hello World", "h") # 1
single_letter_count("Hello World", "z") # 0
single_letter_count("HelLo World", "l") # 3
'''

#define single_letter_count below:
#In my solution, I use the built-in count()  to count the number of times letter  
# appears in string .  I also downcase both string  and letter  to make it 
# case-insensitive (you could also upcase both instead)

def single_letter_count(string,letter):
    return string.lower().count(letter.lower()) 

print(single_letter_count("Hello World", "w")) # 1
print(single_letter_count("Hello World", "h")) # 1
print(single_letter_count("HeLlo World", "L")) # 1