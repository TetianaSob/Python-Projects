# functions_math.py

#function 1 (+)

def add(a,b):
    return a+b

print(add(1,7)) # 8

print("\n")
#########

#function 2 (-)

def subtract(a,b):
    return a-b

print(subtract(9,7)) # 2

print("\n")
######### functiond within the function

def math(a,b, fn=add):
    return fn(a,b)

print(math(1,3)) # 4