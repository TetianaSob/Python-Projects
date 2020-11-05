# remove()
first_list = [1,2,3,4,4,4]
first_list.remove(2)
print(first_list) # [1, 3, 4, 4, 4]

first_list.remove(4)
print(first_list) # [1, 3, 4, 4]

############

items = [1,2,3,4,5]
print(items.pop(1)) # 2

first = items.pop(0)
print(first) # 1

print(items) # [3, 4, 5]

#########

names = ["colt", "blue", "arya", "lena", "colt", "selena", "pablo"]
names.remove("blue")
print(names) # ['colt', 'arya', 'lena', 'colt', 'selena', 'pablo']

