# Lambda_filter_ex-63.py
''' Filter Exercise

Write a function called 'remove_negatives' that accepts 
a list of numbers and returns a copy of the lists with all negative 
numbers removed. Use filter() in your implementation, not
a list comprehansion'''

'''remove_nagatives([-1,3,4,-99])'''
'''remove_nagatives([-7,0,1,2,3,4,5])'''
'''remove_nagatives([50,60,70])'''

def remove_negatives(l):
    return list(filter(lambda n: n >= 0, l))
print(remove_negatives([-1,3,4,-99])) # [3, 4]

# example with lumbda
'''Removing Negatives Solution
I define remove_negatives, which accepts a list I call nums
Then I call filter, passing the nums list and a lambda which returns True if an item is greater or equal to 0.
This filters out all the values that are negative
However filter doesn't return a list, so I have to cast it into a list and then return it'''

def remove_negatives2(nums):
    return list(filter(lambda l: l >= 0, nums))
print(remove_negatives2([-7,0,1,2,3,4,5])) # [0, 1, 2, 3, 4, 5]
