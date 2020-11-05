# Lambda_built_in_functions_any.py

# any()

print(any([0,1,2,3])) # True

print("\n")

print(any([val for val in [1,2,3] if val > 2])) # True

print("\n")

print(any([val for val in [1,2,3] if val > 5])) # False

print("\n")
#########
# ex 2

nums = [2,60, 26, 18, 21]
print(all([num % 2 == 1 for num in nums])) # False

# for person in people:
#     if person[0] != "C"

########

people = ["Charlie", "Casey", "Cody", "Carly", "Cristina"]
print(all(name[0] == 'C' for name in people))

################

# Ex with the list comprehanssion

import sys

list_comp = sys.getsizeof()