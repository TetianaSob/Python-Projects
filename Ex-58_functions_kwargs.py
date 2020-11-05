# Ex-58_functions_kwargs.py

''' **kwargs Exercise '''
''' Note: for this exercise, make use of **kwargs. No default parameters allowed!
Write a function called 'combine_words' which accepts a single string called word
and any number of additional key word arguments. 

If a prefix is provided, return the prefix followed by the word. 
If a suffix is provided, return the word followed by the suffix. 
If neither is provided, just return the word.

It might sound confusing, but the examples should make this a lot clearer!'''

'''combine_words solution'''

'''I check if kwargs contains "prefix".
If it does, I return the value of prefix + the word
Otherwise, I check to see if "suffix" was provided as a kwarg
If it was, I return the word followed by the value of suffix
Otherwise, I just return the word on its own.'''

def combine_words(word,**kwargs):
    if 'prefix' in kwargs:
        return kwargs['prefix'] + word
    elif 'suffix' in kwargs:
        return word + kwargs['suffix']
    return word

print(combine_words("child")) # child
print(combine_words("child", prefix="man")) # manchild
print(combine_words("child", suffix="ish")) # childish
print(combine_words("word", suffix="er")) # worder