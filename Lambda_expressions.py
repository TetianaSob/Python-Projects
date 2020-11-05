# Lumbda_expressions.py

def square(num):
    return num * num
print(square(9)) # 81

print("\n")

# lumbda
# the same function but with lambda
square2 = lambda num: num * num
print(square2(9)) # 81

#Ex-2

add = lambda a,b: a + b
print(add(3,10)) # 13

# print(square.__name__)
# print(square2.__name__)
# print(add.__name__)