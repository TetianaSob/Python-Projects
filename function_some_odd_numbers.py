# function_some_odd_numbers.py

def sum_odd_numbers(numbers):
    total = 0
    for num in numbers:
        if num % 2 != 0:
            total += num
    return total

print(sum_odd_numbers([1,2,3,4,5,6,7])) # 16

print("\n")
#############

def is_odd_number(num):
    if num % 2 != 0:
        return True
    else:
        return False

print(is_odd_number(3)) # True
print(is_odd_number(4)) # False