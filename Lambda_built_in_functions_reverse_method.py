# Lambda_built_in_functions_reverse_method.py

nums = [1,2,3,4]
nums.reverse()
print(nums) # [4, 3, 2, 1]

print(list(reversed("Hello"))) # ['o', 'l', 'l', 'e', 'H']

print("\n")

print(list(reversed([1,2,3,4]))) # [4, 3, 2, 1]

print("\n")
#########

for char in reversed("hello world"):
    print(char)

# d
# l
# r
# o
# w

# o
# l
# l
# e
# h

### using slice
print("hello"[::-1]) # olleh

print("\n")

print(list(reversed("hello"))) # ['o', 'l', 'l', 'e', 'h']

print(''.join(reversed("hello"))) # olleh