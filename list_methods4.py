# index
numbers = [5,6,7,8,9,10]

print(numbers.index(6)) # 1
print(numbers.index(9)) # 4

#########
print("\n")

numbers = [5,5,6,7,8,8,9,10]
print(numbers.index(5)) # 0
print(numbers.index(5, 1)) # 1
print(numbers.index(8, 2)) # 4

#########
print("\n")

names = ["colt", "blue", "arya", "lena", "colt", "selena", "pablo"]
print(names.index("colt")) # 0
print(names.index("colt", 1)) # 4

######### Count()

print("\n")
#** count()
numbers = [1,2,3,4,3,2,1,4,10,2]
print(numbers.count(2)) # 3
print(numbers.count(21)) # 0
print(numbers.count(3)) # 2

print("\n")

print(names.count("colt")) #2
print(names.count("pablo")) # 1

