#dictionary_methods3.py

#update

first = dict(a=1, b=2, c=3, d=4, e=5)
second = {}

second.update(first)
print(second) # {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}


##############

instructor = {
    "name": "Colt",
    "owns_dog": True,
    "num_courses": 4,
    "favourite_language": "Python",
    "is_hilarious": False,
    44: "my favourite number!"
}

person = {"city": "Antigua"}
person.update(instructor)

print("\n")

print(instructor) 
#{'name': 'Colt', 'owns_dog': True, 'num_courses': 4, 'favourite_language': 'Python', 
# 'is_hilarious': False, 44: 'my favourite number!'}

print("\n")

print(person) 
# {'city': 'Antigua', 'name': 'Colt', 'owns_dog': True, 
#'num_courses': 4, 'favourite_language': 'Python', 'is_hilarious': False, 
#44: 'my favourite number!'}

person['name'] = 'Evelia'

print("\n")

print(person) 
# {'city': 'Antigua', 'name': 'Evelia', 'owns_dog': True, 
#'num_courses': 4, 'favourite_language': 'Python', 'is_hilarious': False, 
#44: 'my favourite number!'}

print("\n")

person.update(instructor)
print(person)

# {'city': 'Antigua', 'name': 'Colt', 'owns_dog': True, 'num_courses': 4, 
# 'favourite_language': 'Python', 'is_hilarious': False, 44: 
# 'my favourite number!'}