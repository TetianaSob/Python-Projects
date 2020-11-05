# Ex_65_min_max.py

'''Extremes Exercise - Using Min and Max

Write a fucntion called 'extremes' which accepts an iterable. It should 
return a tuple containing the minumum and the maximum elements. For example:
'''
'''extremes([1,2,3,4,5])'''
'''extremes(99,25,30,-27)'''

# Define extremes below:

# def extremes(l)
# return max([l])
# return min([l])
# print(extremes[1,2,3,4,5]) 


'''Extremes Solution
This solution is pretty straightforward:

I call min(nums) and max(nums)
I wrap the values I get back in a new tuple and return it!'''

def extremes(nums):
    return(min(nums), max(nums))

#print(extremes([1,2,3,4,5]))  # (1, 5)
print(extremes((99,25,30,-27)))  # (-27, 99)