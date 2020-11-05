# Ex-68_Build_in_methods_sum_floats.py

#sum_floats()

'''Write a function called sum_floats. This function should
accept a variable number of arguments. The function should return the sum
of all paramenters that are floats. 
If there are no floats the function should return 0.'''

'''
sum_floats(1.5, 2.4, 'awesome', [], 1) # 3.9
sum_floats(1,2,3,4,5) # 0
'''

# def sum_floats(*nums):
#     return sum(float(nums) for num in nums)

# print(sum_floats(1.5, 2.4, 'awesome', [], 1))

'''Sum Floats Solution
Write a function called sum_floats. This function should accept a variable number of arguments. The function should return the sum of all the parameters that are floats. If there are no floats the function should return 0

I started by defining sum_floats , which accepts any number of arguments using *args 
Much like the previous exercise, I use a generator expression to extract the values in args where type()  is float.
I pass those values in to sum  and return the result.'''


def sum_floats(*args):
    return sum(arg for arg in args if type(arg) == float)

print(sum_floats(1,2,3,4,5)) # 0
print(sum_floats(1.2,2,3,4,5)) # 1.2
print(sum_floats(1.2, 2.6, 3.1, 4, 5)) # 6.9