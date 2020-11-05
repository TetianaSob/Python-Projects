# Ex-45_functions.py
''' last_element'''

'''Write a fumction called last_element. This function takes in one parameter (a list)
and returns a last value in the list. It should return None if the list in empty.'''
'''
last_element([1,2,3]) # 3
last_element([]) # None
'''

#First check to see if the list exists (if it has data in it).  If it does, return the -1 item (last item).  Otherwise, return None.

def last_element2(l):
    if l:
        return l[-1]
    return None

print(last_element2([1,2,3,4,5,6]))  # 6  