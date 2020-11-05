# ex-40.py
#Using string concatenation:

def yell(word):
    return word.upper() + "!"
#Using the string format() method:

print(yell("hi")) # HI!

print("\n") 
##########

def yell(word):
    return "{}!".format(word.upper())

print(yell("nice")) # NICE!

print("\n") 
##########

def yell(word):
    return f"{word.upper()}!"

print(yell("good")) # GOOD!

print("\n")     