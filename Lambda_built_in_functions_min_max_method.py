# Lambda_built_in_functions_min_max_method.py

# min()

print(min([3,4,1,2])) # 1
print(min((1,2,3,4))) # 1
print(min('awesome')) # a
print(min({1: 'a', 3: 'c', 2: 'b'})) #  1

print("\n")
# max()

print(max(3,67,99)) # 99
print(max('c', 'd', 'a')) # d

print(max([3,4,1,2])) # 4
print(max(1,2,3,4)) # 4
print(max('awesome')) # w

print("\n")
##########

nums = [40,32,8,5,10]
print(max(nums)) # 40
print(min(nums)) # 5
print(max("hello world")) # w
print(min("hello world")) # ' ' empty space

# print max for tuple
print(max(3,4,9,1,4)) # 9

#######

names = ['Arya', "Samson", "Dora", "Tim", "Olliver"]

print(min(names)) # Arya
print(max(names)) # Tim

print(min(len(name) for name in names)) # 3

print("\n")

print(max(names, key=lambda n:len(n))) # Olliver

print(min(names, key=lambda n:len(n))) # Tim

print("\n")


#######

songs = [
    {"title": "happy birthday", "playcount": 1},
    {"title": "Survive", "playcount": 6},
    {"title": "YMCA", "playcount": 99},
    {"title": "Toxic", "playcount": 31}
]

print(min(songs, key=lambda s: s['playcount'])) # {'title': 'happy birthday', 'playcount': 1}
print(max(songs, key=lambda s: s['playcount'])) # {'title': 'YMCA', 'playcount': 99}

print(max(songs, key=lambda s: s['playcount'])['title']) # YMCA

#######

# max = 0
# for song in songs
#     if song['playcount'] > max
#         max = song['playcount']
# print(song)

