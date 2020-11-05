#reverse()

first_list = [1,2,3,4]
first_list.reverse()
print(first_list) # [4, 3, 2, 1]

names = ["colt", "blue", "arya", "lena", "colt", "selena", "pablo"]
names.reverse()
print(names) # ['pablo', 'selena', 'colt', 'lena', 'arya', 'blue', 'colt']

#sort()
another_list = [6,4,1,2,5]
another_list.sort()
print(another_list) # [1, 2, 4, 5, 6]

#####
names = ["colt", "blue", "arya", "lena", "colt", "selena", "pablo"]
names.sort()
print(names) # ['arya', 'blue', 'colt', 'colt', 'lena', 'pablo', 'selena']

names.append("ARYA")
names.sort()
print(names) # ['ARYA', 'arya', 'blue', 'colt', 'colt', 'lena', 'pablo', 'selena']

####### join()

words = ['Coding', "Is", "Fun!"]
' '.join(words)
print(words) # ['Coding', 'Is', 'Fun!']

##########

name = ['Mr', "Steele"]
'. '.join(name)
print(name) # ['Mr', 'Steele']

############

names = ["colt", "blue", "arya", "lena", "colt", "selena", "pablo"]
friends = ", ".join(names)
print(friends) # colt, blue, arya, lena, colt, selena, pablo

