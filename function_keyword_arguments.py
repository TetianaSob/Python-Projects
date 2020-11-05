# function_keyword_arguments.py

def full_name(first, last):
    return "Your name is {first} {last}"

print(full_name('Colt', 'Steele'))

print("\n")
#################

def exponent(num, power=2):
    return num ** power

print(exponent(2,3)) # 8
print(exponent(3)) # 9
print(exponent(7)) # 49

print(exponent(power=3, num=4))  # 64