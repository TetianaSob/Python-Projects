# Errors_Raise_Error.py

#raise NameError("blah")

'''File "d:/MY STUFF/Online courses/Python/FirstProgram/Errors_Raise_Error.py", line 3, in <module> 
    raise NameError("blah")'''

#print(NameError) # NameError: blah
'''
def colorize(text, color):
    colors = ("cyan", "yellow", "blue", "green", "magenta")
    if type(text) is not str:
        raise TypeError("text must be instance of string")
    print(f"Printed {text} in {color}")

colorize("hello", "red") # Printed hello in red
colorize(34, "red") # TypeError: text must be instance of string

'''

'''File "d:/MY STUFF/Online courses/Python/FirstProgram/Errors_Raise_Error.py", line 3, in <module> 
    raise NameError("blah")'''

#print(NameError) # NameError: blah

def colorize(text, color):
    colors = ("cyan", "yellow", "blue", "green", "magenta")
    if type(text) is not str:
        raise TypeError("text must be instance of string")
    if color not in colors:
        raise ValueError("color is invalid color")
    print(f"Printed {text} in {color}")

#colorize("hello", "red") # ValueError: color is invalid color
#colorize("hello", 10) # ValueError: color is invalid color
colorize([], 10) #TypeError: text must be instance of string

