# Lambda_built_in_functions_abs_sum_round_method.py

#abs()
 
print(abs(-5)) # 5
print(abs(5)) # 5

print("\n")

print(abs(3.4444)) # 3.4444

print(abs(float('20'))) # 20.0

#####
#fabs()

import math

print(math.fabs(-4)) #4.0

#####
#sum()
''' takes an interable and an optional start
 Returns the sum of start and the items of an iterable from left
 to right and returns the total '''

print(sum([1,2,3])) # 6

print("\n")

print(sum([1,2,3], 10)) # 16
print(sum([1,2,3], -6)) # 0

print(sum((1,3, 4.6))) # 8.6

print("\n")

print(sum({1,3,4,75})) # 83

print(''.join(['hi ', 'there'])) # hi there

#####
#round()
print("\n")

print(round(10.2)) # 10
print(round(1.44444432)) # 1
print(round(1.44444432, 2)) # 1.44


