# Generators_Expressions2.py
import time
gen_start_time = time.time()
print(sum(n for n in range(1000))) # 499500
gen_time = time.time() - gen_start_time

list_start_time = time.time()
print(sum(n for n in range(1000))) # 499500
list_time = time.time() - list_start_time
print(gen_time) # 0.000997304916381836


print(f"sum(n for n in range(1000) took: {gen_time}")  # sum(n for n in range(1000) took: 0.0
print(f"sum(n for n in range(1000) took: {list_time}")  # sum(n for n in range(1000) took: 0.0009968280792236328

print("\n")

print(sum(n for n in range(1000000))) # 499999500000
print(sum([n for n in range(1000000)])) # 499999500000

