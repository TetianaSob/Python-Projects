# Ex-55_functions.py

'''intersection'''

''' Write a function called intersection. This function should accept two lists
and return an list with the values that are bothe input lists. '''


# flesh out intersection pleaseeeee
# Manual Looping Solution
# Here's one potential solution:

# Define an empty list that will eventually store the in common values
# Loop through one list (l1)
#v For each value, check if that value is in the other list (l2)
# If it is, append the value to the in_common list
# Return in_common  after the loop ends
def intersection(l1, l2):
    in_common = []
    for val in l1:
        if val in l2:
            in_common.append(val)
    return in_common

print(intersection([1,2,3], [2,3,4])) # [2, 3]

##############

#List Compt solution is perfectly valid.  It's a more "traditional" way of solving the problem.  A more Python-ic solution involves using a list comprehension to do the same thing on a single line. Both work just as well.  It's a matter of personal preference, so don't get too caught up in it!

def intersection2(l1, l2):
    return [val for val in l1 if val in l2]

print(intersection2([1,2,3], [2,3,4])) # [2, 3]
   
##############

def intersection3(list1, list2):
    return [val for val in set(list1) & set(list2)]   

print(intersection3([1,2,3], [2,3,4])) # [2, 3]