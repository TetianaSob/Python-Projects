# dictionaries_access_data.py

instructor = {
    "name": "Colt",
    "owns_dog": True,
    "num_courses": 4,
    "favourite_language": "Python",
    "is_hilarious": False,
    44: "my favourite number!"
}

print(instructor["name"]) # Colt
print(instructor["thing"]) # KeyError: 'thing'

#################
