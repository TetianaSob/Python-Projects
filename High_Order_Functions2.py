# High_Order_Functions2.py

from random import choice

def greet(person):
    def get_mood():
        msg = choice(('Hello there ', 'Go away ', 'I love you '))
        return msg

    result = get_mood() + person
    return result

print(greet("Toby"))
# Go away Toby
# I love you Toby
# Go away Toby
# Hello there Toby
