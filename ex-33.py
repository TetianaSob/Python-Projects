person = [["name", "Jared"], ["job", "Musician"], ["city", "Bern"]]

# use the person variable in your answer
answer = {key: value for key, value in person}

print(answer) # {'name': 'Jared', 'job': 'Musician', 'city': 'Bern'}

print("\n")
#######

person = [["name", "Jared"], ["job", "Musician"], ["city", "Bern"]]
answer2 = {thing[0]: thing[1] for thing in person}
print(answer2) # {'name': 'Jared', 'job': 'Musician', 'city': 'Bern'}

print("\n")
#######

person = [["name", "Jared"], ["job", "Musician"], ["city", "Bern"]]
answer3 = {k:v for k,v in person}
print(answer3) # {'name': 'Jared', 'job': 'Musician', 'city': 'Bern'}

print("\n")
#######

person = [["name", "Jared"], ["job", "Musician"], ["city", "Bern"]]
answer4 = dict(person)
print(answer4) # {'name': 'Jared', 'job': 'Musician', 'city': 'Bern'}


