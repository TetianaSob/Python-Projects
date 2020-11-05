# Generators_Expressions.py

def nums():
    for num in range(1,10):
        yield num

g = nums()
print(next(g)) # 1
print(next(g)) # 2
print(next(g)) # 3

print("\n")

g1 = (num for num in range(1,10))

print(next(g1)) # 1
print(next(g1)) # 2
print(next(g1)) # 3

print("\n")

l = [n for n in range(1,10)]
print(l) # [1, 2, 3, 4, 5, 6, 7, 8, 9]

