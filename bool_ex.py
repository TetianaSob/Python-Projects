x = 13
y =  13

print(bool(x == y)) # True
print(bool(x is y)) # True

######

a = [1,2]
b = [1,2]

print(bool(a == b)) # True
print(bool(a is b)) # False

clone = a
print(a is clone) # True