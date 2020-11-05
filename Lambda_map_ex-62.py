# Lambda_map_ex-62.py

'''Map Time Exercise

Write a functiomn called 'decrement_list' that accepts a single list of numbers as
a parameter. It should return a copy of the list where each item 
has been decremented by one. Use map to do this!. For example:
"decrement_list([1,2,3])"
"decrement_list([20,14,11])" '''

nums = [1,2,3]
decrement_list = list(map(lambda x: x-1, nums))
print(decrement_list) # [0, 1, 2]

print("\n")
####

#Ex-2
l = [20,2,3]
def decrement_list(l):
    return list(map(lambda n: n-1, l))

print(decrement_list) # <function decrement_list at 0x038ED2F8>

doubles = map(lambda x: x*2, l)
for num in doubles:
    print(num)

# 40
# 4
# 6