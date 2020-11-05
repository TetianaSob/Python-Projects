# function_args.py

def sum_all_nums(num1, num2, num3):
    return num1 + num2 + num3

print(sum_all_nums(4,6,7)) # 17 

# *** to not have a limit of args(argulents) use (*args)
def sum_all_nums2(*args):
    print(args)

sum_all_nums2(1,4,5,9,6,4) # (1, 4, 5, 9, 6, 4) -it is a tuple

##############

def sum_all_nums3(*args):
    total = 0
    for num in args:
        total += num
    return total

print(sum_all_nums3(1,3,4,5)) # 13
print(sum_all_nums3(1,4,5,9,6,4)) # 29

################

def ensure_correct_info(*args):
    if "Colt" in args and "Steele" in args:
        return "Welcome back Colt!"
    
    return "Not sure who you are..."

print(ensure_correct_info()) # Not sure who you are...

print(ensure_correct_info(1, True, "Steele", "Colt")) # Welcome back Colt!

print(ensure_correct_info("hello", False, 78)) # Not sure who you are...

################

def sum_all_nums4(*nums):
    total = 0
    for num in nums:
        total += num
    return total

print(sum_all_nums4(3,5,64,3,3)) # 78
