# methods
data = [1,2,3]

# **  append()
first_list = [1,2,3,4]
first_list.append(5)
print(first_list)  # [1, 2, 3, 4, 5]

print("\n")

# ** extend
first_list = [1,2,3,4]
first_list.append([5,6,7,8])
print(first_list)  # [1, 2, 3, 4, [5, 6, 7, 8]]

print("\n")

corect_list = [1,2,3,4]
corect_list.extend([5,6,7,8])
print(corect_list) # [1, 2, 3, 4, 5, 6, 7, 8] 
#print(data.sort())

print("\n")

#print(data.append())

nums = [1,2,3]
print(len(nums)) # 3

nums.append([4,5])
print(len(nums))
print(nums)  # [1, 2, 3, [4, 5]]

nums.extend([4,5])
print(len(nums)) # 6
print(nums) # [1, 2, 3, [4, 5], 4, 5]

#** Insert

print("\n")

first_list = [1,2,3,4]
first_list.insert(2, "Hi!")
print(first_list) # [1, 2, 'Hi!', 3, 4]

first_list.insert(-1, 'The end!')
print(first_list) # [1, 2, 'Hi!', 3, 'The end!', 4]

#to insert to the end
nums = [1,2,3,4]
nums.insert(len(nums), "LAST") 
print(nums) # [1, 2, 3, 4, 'LAST']