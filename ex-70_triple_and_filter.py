# ex-70_triple_and_filter.py

'''Write a function called triple_and_filter. This function should accept
a list of numbers folter out every number that is not divesible by 4, 
and return a new list where every remaining number is tripled.'''

'''
triple_and_filter([1,2,3,4]) # [12]
triple_and_filter([6,8,10,12]) # [24,36]
'''

def triple_and_filter(l):
    return list(filter(lambda x: x % 4 == 0, l))

print(triple_and_filter([1,2,3,4])) # [4]

print("\n")
#####

'''Triple and Filter Solution
For my solution, I chose to use map and filter in combination.'''

def triple_and_filter(lst):
    return list(filter(lambda x: x % 4 == 0, map(lambda x: x*3, lst)))

print(triple_and_filter([1,2,3,4])) # [12]
print(triple_and_filter([6,8,10,12])) # [24, 36]