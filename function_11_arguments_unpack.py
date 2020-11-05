# function_11_arguments_unpack.py

def display_names(first, second):
    print(f"{first} says hello to {second}")

names = {"first": "Colt", "second": "Rusty"}
display_names(first="Charlie", second = "Sue") # Charlie says hello to Sue

print("\n")

# version 2 with '**args' (to unpack dictionaries into keyword arguments)

def display_names(first, second):
    print(f"{first} says hello to {second}")

names = {"first": "Colt", "second": "Rusty"}
display_names(**names) # Colt says hello to Rusty

print("\n")

# 1 star * (to unpack tuples, lists)

def sum_all_values(*args):
    print(args)
    total = 0
    for num in args:
        total += num
    print(total) # 21

nums = [1,2,3,4,5,6]
sum_all_values(*nums) # (1, 2, 3, 4, 5, 6)

print("\n")
#Ex-2

def add_and_multiply_numbers(a,b,c):
    print(a + b * c)

data = dict(a=1, b=2, c=3)

#add_and_multiply_numbers(data)
add_and_multiply_numbers(**data) # 7

print("\n")
#Ex-3

def add_and_multiply_numbers2(a,b,c, **kmwargs):
    print(a + b * c)
    print("OTHER STUFF...") # OTHER STUFF...
    print(kmwargs) # {}

data = dict(a=1, b=2, c=3)

#add_and_multiply_numbers(data)
add_and_multiply_numbers2(**data) # 7

print("\n")
#Ex-4

def add_and_multiply_numbers2(a,b,c, **kmwargs):
    print(a + b * c)
    print("OTHER STUFF...") # OTHER STUFF...
    print(kmwargs) # {'d': 55, 'name': 'Tony'}

data = dict(a=1, b=2, c=3, d=55, name="Tony")

#add_and_multiply_numbers(data)
add_and_multiply_numbers2(**data) # 7

print("\n")
#Ex-5

def add_and_multiply_numbers2(a,b,c, **kmwargs):
    print(a + b * c)
    print("OTHER STUFF...") # OTHER STUFF...
    print(kmwargs)  # {'d': 55, 'name': 'Tony', 'cat': 'Blue'}

data = dict(a=1, b=2, c=3, d=55, name="Tony")

#add_and_multiply_numbers(data)
add_and_multiply_numbers2(**data, cat = "Blue") # 7