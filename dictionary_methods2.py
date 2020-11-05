#dictionary_methods.py

d= dict(a=1, b=2, c=3)
# print(d.pop())
print(d.pop('a')) # 1

print("\n")

print(d) #{'b': 2, 'c': 3}

print("\n")

#print(d.pop('e')) # KeyError


############
# pop()

instructor = {
    "name": "Colt",
    "owns_dog": True,
    "num_courses": 4,
    "favourite_language": "Python",
    "is_hilarious": False,
    44: "my favourite number!"
}

instructor.pop("owns_dog")
print(instructor)
#{'name': 'Colt', 'num_courses': 4, 'favourite_language': 'Python', 
# 'is_hilarious': False, 44: 'my favourite number!'}


############
# popitem

d = dict(a=1, b=2, c=3, d=4, e=5)
d.popitem() # {'a': 1, 'b': 2, 'c': 3, 'd': 4}
print(d)

