#dictionaries_access_data2.py

instructor = {
    "name": "Colt",
    "owns_dog": True,
    "num_courses": 4,
    "favourite_language": "Python",
    "is_hilarious": False,
    44: "my favourite number!"
}

print(instructor["name"]) # Colt
print(instructor["owns_dog"]) # True
print(instructor["num_courses"]) # 4
print(instructor["favourite_language"]) # Python
print(instructor["is_hilarious"]) # False
print(instructor[44]) # my favourite number!

print("\n")
############
#For loop

instructor = {
    "name": "Colt",
    "owns_dog": True,
    "num_courses": 4,
    "favourite_language": "Python",
    "is_hilarious": False,
    44: "my favourite number!"
}

for value in instructor.values():
    print(value)

# Colt
# True
# 4
# Python
# False
# my favourite number!

print("\n")
############

print(instructor.values()) # dict_values(['Colt', True, 4, 'Python', False, 'my favourite number!'])

print("\n")
############

for v in instructor.values():
    print(v)

# Colt
# True
# 4
# Python
# False
# my favourite number!

print("\n")
############

print(instructor.keys()) # dict_keys(['name', 'owns_dog', 'num_courses', 'favourite_language', 'is_hilarious', 44])

###########

for k,v in instructor.items():
    print(f"key is {k}, value is {v}") 

# key is name, value is Colt
# key is owns_dog, value is True
# key is num_courses, value is 4
# key is favourite_language, value is Python
# key is is_hilarious, value is False
# key is 44, value is my favourite number!    