# Lambda_map_function.py

nums = [2,4,6,8,10]

doubles = map(lambda x: x*2, nums)
for num in doubles:
    print(num)

# 4
# 8
# 12
# 16
# 20

print(list(nums)) # [2, 4, 6, 8, 10]

print("\n")
#####

#Ex-2

people = ["Darcy", "Christina", "Dana", "Annabel"]
peeps = map(lambda name: name.upper(), people)
print(list(peeps)) # ['DARCY', 'CHRISTINA', 'DANA', 'ANNABEL']

print("\n")
####

#Ex-3

l = [1,2,3,4]
doubles = list(map(lambda x: x*2, l))
print(doubles) # [2, 4, 6, 8]

print("\n")
####

#Ex-4

names = [
    {'first': 'Rusty', 'last': 'Steele'},
    {'first': 'Colt', 'last': 'Steele'},
    {'first': 'Blue', 'last': 'Steele'}
]

first_names = list(map(lambda x: x['first'], names))
print(first_names) # ['Rusty', 'Colt', 'Blue']

print("\n")
####

#Ex-5

def double(x): return x*2
print(double(3)) # 6

print("\n")
####

num2 = [3,5,7,8,9]
doubles2 = map(double, nums)
print(list(doubles))   # [2, 4, 6, 8]
doubles = list(map(lambda x: x*2, nums))
print(doubles)    # [4, 8, 12, 16, 20]