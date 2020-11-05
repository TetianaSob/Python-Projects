# Ex-56_functions.py

'''partition'''

'''Write a function called partition. This function accepts a list and a callback
function (which you can assume returns 'True' or 'False).

The function should iterate over each element in the list and invoke the callback
function at each iteration.

- If the result of the callback function is 'True', the element should go into 
the first (i.e the 'truthy' list).
- If the result of the callback function is 'False', the element should go into 
the second list ( i.e the 'falsy' list)

When it's finished, partition should return both lists of one langer list, like so:
[truthy_list, falsy_list] '''

def partition(lst, fn):
    trues = []
    falses = []
    for val in lst:
        if fn(val):
            trues.append(val)
        else:
            falses.append(val)
    return [trues, falses]

print(partition([1,2,3,4], isEven)) # [[2,4],[1,3]])

#############

#List Comprehension Version
#Using a list comprehension, you can get this function down to a single line.  It's definitely a tradeoff though.  It's much short but also more difficult to understand.  It's a fine balance between brevity and readability. 

def partition2(lst, fn):
    return [[val for val in lst if fn(val)], [val for val in lst if not fn(val)]]

print(partition2([1,2,3,4], isEven))

#Another Solution
#This solution was submitted by a student named Jonathan.  Thanks, Jonathan!

def partition3(l, callback):
    return [[l.pop(l.index(i)) for i in l if callback(i)],l]

print(partition3([1,2,3,4], isEven))