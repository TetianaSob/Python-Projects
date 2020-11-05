# Ex-72_Debugging_Error_Handling.py

# Write a function called divide, which accepts two parameters (you can call them num1 and num2). The function should return the result of num1 divided by num2. If you do not pass the correct amount of arguments to the function, it should return the string "Please provide two integers or floats". If you pass as the second argument a 0, Python will raise a ZeroDivisionError, so if this function is invoked with a 0 as the value of num2, return the string "Please do not divide by zero"

    # Examples
'''  
def divide(num1, num2):
  
    try:
        return num1/num2
    except TypeError:
        print("Please provide two integers or floats")     
    except ZeroDivisionError:
        print("Please do not divide by zero")

print(divide(4,2))
'''
################

'''Division Exercise Solution
Here's my version of the divide function:'''

def divide2(a,b):
    try:
        total = a / b
    except TypeError:
        return "Please provide two integers or floats"
    except ZeroDivisionError:
        return "Please do not divide by zero"
    return total
