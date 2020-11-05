# Ex-67_Build_in_methods_sum_even_values.py

#sum_even_values
'''Write a function called sum_even_values. This function should accept a variable number
of arguments and return the sum of all the arguments that are divisible by 2.
If there are no numbers divisible by 2, the function should return 0.
To be clear, it accepts all the numbers as individual arguments!. '''

'''
sum_even_values(1,2,3,4,5,6) # 12
sum_even_values(4,2,1,10) # 16
sum_even_values(1) # 0
'''

# # define sum_even_values
# def sum_even_values(nums):
#     return (sum(num) for num in nums)

# print(sum_even_values([1,2,3,4,5,6]))

'''Sum Even Values Solution
I define a function called sum_even_values  which accepts any number of arguments, thanks to *args 
I grab the even numbers using the generator expression (arg for arg in args if arg % 2 == 0)  (could also use a list comp)
I pass the even numbers I extracted into sum()  and return the value
The default start value of sum()  is 0, so I don't have to do anything special to get it to return 0 if there are no even numbers!
'''

def sum_even_values(*args):
    return sum(arg for arg in args if arg % 2 == 0)
print(sum_even_values(1,2,3,4,5,6)) # 12
print(sum_even_values(4,2,1,10)) # 16

