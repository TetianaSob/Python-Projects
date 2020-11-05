# High_Order_Functions3.py

from random import choice

def make_laugh_func():
    def get_laugh():
        l = choice(('HAHAHAH', 'lol', 'tehehe'))
        return l

    return get_laugh

laugh = make_laugh_func()
print(laugh()) 
# tehehe
# lol
# tehehe

print("\n")

#########

def make_laugh_at_func2(person):
    def get_laugh():
        laugh = choice(('HAHAHAH', 'lol', 'tehehe'))
        return f"{laugh} {person}"

    return get_laugh

laugh_at = make_laugh_at_func2("Linda")
print(laugh_at()) 

# lol Linda
# HAHAHAH Linda
# lol Linda