# function_10_unpack.py

def sum_all_values(*args):
    print(args) # ()
    total = 0
    for num in args:
        total += num
    print(total) # 11

#print(sum_all_values(1,2,5,3)) # None

print("\n")
#############

nums = [1,2,3,4,5,6] # 0
print(sum_all_values(*nums)) # 21
#print("\n")

#print(sum_all_values(*nums)) # None