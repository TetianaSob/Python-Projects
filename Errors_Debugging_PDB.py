# Errors_Debugging_PDB.py

'''
import pdb

first = "First"
second = "Second"

pdb.set_trace() # put it right before the breaking lines

result = first + second
third = "Third"
result += third
print(result)

'''
'''
#############
#pdb Gotcha

def add_numbers(a,b,c,d):
    import pdb; pdb.set_trace()

    return a + b + c + d
print(add_numbers(1,2,3,4))

#print(Pdb(1))
'''