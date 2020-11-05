# Lambda_filter.py

l = [1,2,3,4]
evens = list(filter(lambda x: x % 2 == 0, l))
print(evens)  # [2, 4]

print("\n")
# check by name
# Ex-2

names = ["austin", "penny", "anthony", "angel", "billy"]
a_names = filter(lambda n: n[0]=='a', names)
print(a_names)    # <filter object at 0x014D7250>
print(list(a_names))  # ['austin', 'anthony', 'angel']

print("\n")

# Ex-3
users = [
    {"username": "samuel", "tweets": ["I love cake"]},
    {"username": "katie", "tweets": ["I love my cat"]},
    {"username": "jeff", "tweets": []},
    {"username": "bob123", "tweets": []},
    {"username": "doggo_luvr", "tweets": ["dogs are the best"]},
    {"username": "guitar_gal", "tweets": []}
]

inactive_users = filter(lambda u: len(u['tweets']) == 0, users)
print(list(inactive_users)) 

print("\n")
####

active_users = filter(lambda u: len(u['tweets']) != 0, users)
print(list(active_users)) 

print("\n")
# [{'username': 'jeff', 'tweets': []}, {'username': 'bob123', 
# 'tweets': []}, {'username': 'guitar_gal', 'tweets': []}]

#Ex-2

inactive_users2 = [user["username"].upper() for user in users if not user["tweets"]]
print(inactive_users2)

# ['JEFF', 'BOB123', 'GUITAR_GAL']