# Lambda_filter_map.py

names = ['Lassie', 'Colt', 'Rusty']

print(list(map(lambda name: f"Your instructor is {name}", 
    filter(lambda value: len(value) < 5, names))))

#['Your instructor is Colt']

print("\n")
######

# Ex-3
users = [
    {"username": "samuel", "tweets": ["I love cake"]},
    {"username": "katie", "tweets": ["I love my cat"]},
    {"username": "jeff", "tweets": []},
    {"username": "bob123", "tweets": []},
    {"username": "doggo_luvr", "tweets": ["dogs are the best"]},
    {"username": "guitar_gal", "tweets": []}
]

print(list(map(lambda user: user["username"], users))) 
# ['samuel', 'katie', 'jeff', 'bob123', 'doggo_luvr', 'guitar_gal']
print("\n")

print(list(filter(lambda u: not u['tweets'], users)))
#[{'username': 'jeff', 'tweets': []}, {'username': 'bob123', 'tweets': []}, {'username': 'guitar_gal', 'tweets': []}]

print("\n")
############

usernames = list(map(lambda user: user["username"].upper(),
    filter(lambda u: not u['tweets'], users)))
print(usernames) # ['JEFF', 'BOB123', 'GUITAR_GAL']    

print("\n")
############
#Ex-2

inactive_users2 = [user["username"].upper() for user in users if not user["tweets"]]
print(inactive_users2)

print(usernames) 
# ['JEFF', 'BOB123', 'GUITAR_GAL']

print("\n")
############

names = ['Lassie', 'Colt', 'Rusty']

print(list(map(lambda name: f"Your instructor is {name}",
filter(lambda value: len(value) < 5, names)))) # ['Your instructor is Colt']

