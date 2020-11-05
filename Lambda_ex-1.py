# Lambda_ex-1.py

# Writing your own lambda

''' Write a lambda that a single number and cubes it. Save it in 
the variable called 'cube', 'cube(2)', 'cube(3)', 'cube(8)'.

Write a lambda that accepts a single number and cubes it. Save it in a variable called cube.'''

#def cube(num): return num * num * num
cube = lambda num: num * num * num
print(cube(9)) # 729
print(cube(2)) # 8
print(cube(3)) # 27

print("\n")

#Ex-1
cube = lambda num: num ** 3
print(cube(9)) # 729

#Ex-2

qurdr = lambda num: num ** 4
print(qurdr(2)) # 16
