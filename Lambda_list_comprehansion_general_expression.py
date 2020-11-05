# Lambda_list_comprehansion_general_expression.py

import sys
list_comp = sys.getsizeof([x * 10 for x in range(1000)])
gen_exp = sys.getsizeof(x * 10 for x in range(1000))

print("To do the same thing, it takes...")
print(f"List Comprehension: {list_comp} bytes")
print(f"Generator Expression: {gen_exp} bytes")

# To do the same thing, it takes...
# List Comprehension: 4508 bytes
# Generator Expression: 56 bytes