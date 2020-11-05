#slicing
first_list = [1,2,3,4]
print(first_list[1:]) # [2, 3, 4]
print(first_list[3:]) # [4]
#some_list[start:end:step]

print("\n")

###
colors = ["red", "orange", "yellow", "green", "indigo", "violet"]
print(colors[2]) #yellow

print(colors[2:]) #['yellow', 'green', 'indigo', 'violet']
print(colors[0:]) #['red', 'orange', 'yellow', 'green', 'indigo', 'violet']

print(colors[-2]) #indigo
print(colors[-2:]) #['indigo', 'violet']

first_list = [1,2,3,4]
print(first_list[2:]) # [3, 4]
print(first_list[4:]) # [4]
print(first_list[:4]) # [1, 2, 3, 4]
print(first_list[1:3]) # [2, 3]

###
colors = ["red", "orange", "yellow", "green", "indigo", "violet"]
print(colors[:5]) # ['red', 'orange', 'yellow', 'green', 'indigo']
print(colors[2:4]) # ['yellow', 'green']

print("\n")

second_list = [1,2,3,4,5,6]
print(second_list[1::2]) # [2, 4, 6]
print(second_list[::2]) # [1, 3, 5]
print(second_list[1::-1]) # [2, 1]
print(second_list[2::-1]) # [3, 2, 1]

#########

print("\n")

numbers = [1,2,3,4,5]
numbers[1:3] = ['a','b','c']
print(numbers) # [1, 'a', 'b', 'c', 4, 5]

#########

print("\n")

colors = ["red", "orange", "yellow", "green", "indigo", "violet"]
print(colors[::2]) # ['red', 'yellow', 'indigo']
print(colors[::-1]) # ['violet', 'indigo', 'green', 'yellow', 'orange', 'red']
print(colors[5][::-1]) # teloiv

#########

print("\n")

print("helllooo"[:3]) # hel
print("helllooo"[::3]) # hlo

#########

print("\n")

numbers = [1,2,3,4]
print(numbers[::-1]) # [4, 3, 2, 1]