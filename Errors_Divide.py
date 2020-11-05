# Errors_Divide.py

def devide(a,b):
    try:
        result = a/b
    except ZeroDivisionError:
        print("don't devide by zero please")
    except TypeError as err:
        print("a and b must be ints or floats")
        print(err)
    else:
        print(f"{a} divided by {b} is {result}")

#print(devide(1,2)) # 0.5

#print("\n")

print(devide(1,0)) # don't devide by zero please

print("\n")

print(devide(1,'a')) # a and b must be ints or floats

# a and b must be ints or floats
# unsupported operand type(s) for /: 'int' and 'str'
# None