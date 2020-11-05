# dictionaly_test_accistance.py

instructor = {
    "name": "Colt",
    "owns_dog": True,
    "num_courses": 4,
    "favourite_language": "Python",
    "is_hilarious": False,
    44: "my favourite number!"
}

print("name" in instructor) # True
print("awesome" in instructor) # False

print("\n")

print("name" in instructor.values()) # False