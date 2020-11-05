# Decorators_Speed_Test.py
'''
import time

start_time = time.time()
sum([x for x in range(100)])

total_time = time.time() - start_time
sum(x for x in range(100))
'''
from functools import wraps
from time import time

def speed_test(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        start_time = time()
        result = fn(*args, **kwargs)
        end_time = time()
        print(f"Executing {fn.__name__}")
        print(f"Time Elapsed: {end_time - start_time}")
        return result
    return wrapper

@speed_test
def sum_nums_gen():
    return sum(x for x in range(50000000))

@speed_test
def sum_nums_list():
    return sum(x for x in range(50000000)) # use the list comprehansion

print(sum_nums_gen()) 
# Executing sum_nums_gen
# Time Elapsed: 6.561449289321899
# 1249999975000000

print("\n")

print(sum_nums_list())
# Executing sum_nums_list
# Time Elapsed: 6.243312120437622
# 1249999975000000