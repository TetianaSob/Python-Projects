# function_scope.py

instructor = 'Colt'

def say_hello():
    return f'Hello {instructor}'

print(say_hello()) # Hello Colt    

###########

def say_hello():
    instructor = 'Colt'
    return f'Hello {instructor}'

print(say_hello()) # Hello Colt

print("\n")
##############

instructor1 = "Mary"
def say_hello():
    instructor = 'Colt'
    return f'Hello {instructor1}'

print(say_hello()) # Hello Colt
print("\n")
print(say_hello(instructor1)) # Hello Colt
print(say_hello(instructor2)) # Hello Colt

############### Global Scope

 total = 0

 def increment():
     total += 1
     return total

 print(increment()) # TypeError: say_hello() takes 0 positional arguments but 1 was given

############### Global Scope

total = 0

def increment():
    global total
    total += 1
    return total

print(increment()) 