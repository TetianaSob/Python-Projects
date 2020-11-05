#functions_6.py

def exponent(num, power):
    return num ** power

print(exponent(2, 3)) # 8
print(exponent(3, 2)) # 9

print("\n")
############

def exponent(num, power = 2):
    return num ** power

print(exponent(2)) # 4
print(exponent(3)) # 9