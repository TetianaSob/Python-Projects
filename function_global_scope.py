# function_global_scope.py

total = 0

def increment():
    global total
    total += 1
    return total

print(increment()) # 1

print("\n")
###############

name = "Rusty"

def greet():
    print(name) # Rusty

print(greet()) # None
greet() # Rusty


print("\n")
###############

name = "Rusty"

def greet():
    name = "Rusty Steele"
    print(name) # Rusty

greet() # Rusty Steele

