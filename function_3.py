#function_3.py

def print_square_of_7():
    print(7**2)

print_square_of_7()  # 49   

######
nums = [1,2,3,4]
length = len(nums)
print(length) # 4

last_item = nums.pop()
print(nums) # [1, 2, 3]

###########

def square_of_7():
    print("I AM BEFORE THE RETURN!")
    return 7**2

result = square_of_7()
print(result)
# I AM BEFORE THE RETURN!
#49