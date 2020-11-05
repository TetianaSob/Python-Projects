# Lambda_built_in_functions_sorted_method.py

# returns a new sorted list from the items in iterable

more_numbers = [6,1,8,2]
print(sorted(more_numbers)) # [1, 2, 6, 8]
print(more_numbers) # [6, 1, 8, 2]

print("\n")
#######

nums = [4,6,1,30,55,23]
print(sorted(nums)) # [1, 4, 6, 23, 30, 55]
print(nums) # [4, 6, 1, 30, 55, 23]

print("\n")

# to sort the opposite direction
print(sorted(nums, reverse=True)) # [55, 30, 23, 6, 4, 1]
print(nums) # [4, 6, 1, 30, 55, 23]

print("\n") 

## sort the tuple

print(sorted((1,3,77,2,90))) # [1, 2, 3, 77, 90]

print("\n") 
########## Sort the distionary

users = [
    {"username": "samuel", "tweets": ["I love cake"]},
    {"username": "katie", "tweets": ["I love my cat"]},
    {"username": "jeff", "tweets": [], "color": "purple"},
    {"username": "bob123", "tweets": [], "num": 10, "color": "teal"},
    {"username": "doggo_luvr", "tweets": ["dogs are the best"]},
    {"username": "guitar_gal", "tweets": []}
]

print(sorted(users, key=len))

print("\n")
#[{'username': 'samuel', 'tweets': ['I love cake']}, 
# {'username': 'katie', 'tweets': ['I love my cat']}, 
# {'username': 'doggo_luvr', 'tweets': ['dogs are the best']}, 
# {'username': 'guitar_gal', 'tweets': []}, 
# {'username': 'jeff', 'tweets': [], 'color': 'purple'}, 
# {'username': 'bob123', 'tweets': [], 'num': 10, 'color': 'teal'}]  ## ** it has 3 keys

print(sorted(users, key=lambda user: user['username']))

print("\n")
# [{'username': 'bob123', 'tweets': [], 'num': 10, 'color': 'teal'}, 
# {'username': 'doggo_luvr', 'tweets': ['dogs are the best']}, 
# {'username': 'guitar_gal', 'tweets': []}, 
# {'username': 'jeff', 'tweets': [], 'color': 'purple'}, 
# {'username': 'katie', 'tweets': ['I love my cat']}, 
# {'username': 'samuel', 'tweets': ['I love cake']}]

print(sorted(users, key=lambda user: user['tweets']))

# [{'username': 'jeff', 'tweets': [], 'color': 'purple'}, 
# {'username': 'bob123', 'tweets': [], 'num': 10, 'color': 'teal'}, 
# {'username': 'guitar_gal', 'tweets': []}, 
# {'username': 'samuel', 'tweets': ['I love cake']}, 
# {'username': 'katie', 'tweets': ['I love my cat']}, 
# {'username': 'doggo_luvr', 'tweets': ['dogs are the best']}]

print("\n")

print(sorted(users, key=lambda user: len(user['tweets']), reverse = True))

# [{'username': 'samuel', 'tweets': ['I love cake']}, 
# {'username': 'katie', 'tweets': ['I love my cat']}, 
# {'username': 'doggo_luvr', 'tweets': ['dogs are the best']}, 
# {'username': 'jeff', 'tweets': [], 'color': 'purple'}, 
# {'username': 'bob123', 'tweets': [], 'num': 10, 'color': 'teal'}, 
# {'username': 'guitar_gal', 'tweets': []}]

print("\n")
############

songs = [
    {"title": "happy birthday", "playcount": 1},
    {"title": "Survive", "playcount": 6},
    {"title": "YMCA", "playcount": 99},
    {"title": "Toxic", "playcount": 31}
]

print(sorted(songs, key=lambda song: song['playcount']))

# [{'title': 'happy birthday', 'playcount': 1}, 
# {'title': 'Survive', 'playcount': 6}, 
# {'title': 'Toxic', 'playcount': 31}, 
# {'title': 'YMCA', 'playcount': 99}]

print("\n")

print(sorted(songs, key=lambda song: song['playcount'], reverse=True))

# [{'title': 'YMCA', 'playcount': 99}, 
# {'title': 'Toxic', 'playcount': 31}, 
# {'title': 'Survive', 'playcount': 6}, 
# {'title': 'happy birthday', 'playcount': 1}]