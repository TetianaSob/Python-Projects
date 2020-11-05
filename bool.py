# 2. Is the following expression truthy or falsy?
x = 15
y = 0
x or y
print(bool(x or y))  # True

# 3. Is the following expression truthy or falsy?

x = 0
y = None
x or y  # this expression
print(bool( x or y)) # False
# hint: think about what bool(x or y)  results in


# 4. Is the following expression truthy or falsy?
a = 0
b = 1000
a and b  # this expression
print(bool( a and b)) # False
# hint: think about what bool(a and b)  results in

# 5. Harder question. Is the following expression truthy or falsy?

a = -1
not a  # this expression
print (bool(a)) # False

# 6. Hardest question! Is the following truthy or falsy:

x = 0
y = -1
print(bool(x or y and x - 1 == y and y + 1 == x)) # True
#tip: put parentheses around different logical statements to make it easier to break down  


