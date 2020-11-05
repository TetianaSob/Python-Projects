#list comprehension 2

nums = [1,2,3]
print([x*10 for x in nums]) # [10, 20, 30]
print([x/2 for x in nums]) # [0.5, 1.0, 1.5]

########
numbers = [1,2,3,4,5]
doubled_numbers = []

for num in numbers:
    doubled_number = num * 2
    doubled_numbers.append(doubled_number)

print(doubled_numbers) # [2, 4, 6, 8, 10]

#########
print("\n")

numbers = [1,2,3,4,5]
doubled_numbers = [num * 2 for num in numbers]
print(doubled_numbers) # [2, 4, 6, 8, 10]

##########
