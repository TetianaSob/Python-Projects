# Ex-98_find_and_replace.py

'''
find_and_replace('story.txt', 'Alice', 'Colt') 
# story.txt now contains the first chapter of my new book,
# Colt's Adventures in Wonderland
'''

#Find and Replace Solution

def find_and_replace(file_name, old_word, new_word):
    with open(file_name, "r+") as file:
        text = file.read()
        new_text = text.replace(old_word, new_word)
        file.seek(0)
        file.write(new_text)
        file.truncate()

find_and_replace('story.txt', 'Colt', 'Alice')  
# find_and_replace('story.txt', 'Alice', 'Colt') 

# replaced 'Colt' with 'Alice'

# The story text file
# The additional text
# more 
# more

# additional text
# Alice, 
# 1
# Alice 2        