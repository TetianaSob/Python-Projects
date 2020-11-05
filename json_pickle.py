# json_pickle.py

import jsonpickle

class Cat:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
    
c = Cat("Charles", "Tabby")


# with open("cat.json", "w") as file: # to write to the file

#     frozen = jsonpickle.encode(c)
#     file.write(frozen)

with open("cat.json", "r") as file:
    contents = file.read()
    unfrozen = jsonpickle.decode(contents)
    print(unfrozen) # <__main__.Cat object at 0x030174D8>    

# {"py/object": "__main__.Cat", "name": "Charles", "breed": "Tabby"}