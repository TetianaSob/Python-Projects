#** clear()

first_list = [1,2,3,4]
first_list.clear()
print(first_list) # []

#** pop()
first_list = [1,2,3,4]
first_list.pop()
print(first_list.pop(1)) # 2
print(first_list) # [1, 3]

print("\n")

items = ["socks", "mug", "tea pot", "cat food"]
print(items) # ['socks', 'mug', 'tea pot', 'cat food']
items.pop()
print(items) # ['socks', 'mug', 'tea pot']

last_item = items.pop()
print(last_item) # tea pot
print("\n")

print(items) # ['socks', 'mug']

items.pop(1)
print(items) # ['socks']

###########

first_list = [1,2,3,4]
first_list.pop()
print(first_list) # [1, 2, 3]
first_list.pop(1)
print(first_list) # [1, 3]