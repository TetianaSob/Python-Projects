# Iterators_Generators.py

'''Generators are iterators
Generators can be created with generator functions
Generator functions use the yield keyword
Generators can be created with generator expressions'''

def count_up_to(max):
    count = 1
    while count <= max:
        yield count
        count += 1

counter = count_up_to(5) # <generator object count_up_to at 0x03049610>
print(next(counter)) # 1
print(next(counter)) # 2
print(next(counter)) # 3
print(next(counter)) # 4
print(next(counter)) # 5

print("\n")

counter = count_up_to(7) 
print(next(counter)) # 1
# print(next(counter)) # 2
# print(next(counter)) # 3
# print(next(counter)) # 4
# print(next(counter)) # 5
# print(next(counter)) # 6
# print(next(counter)) # 7
print("\n")

for num in counter:
    print(num)

# 2
# 3
# 4
# 5
# 6
# 7

counter = count_up_to(10)
print(list(counter)) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

