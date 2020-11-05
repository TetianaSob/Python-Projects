# Errors_Handle_Error.py

try:
    footer 
except NameError as err:
    print("PROBLEM!") # PROBLEM!
print("after the try") # after the try

###########

try:
    colt
except:
    print("You tried to use a variable that was never declared!") # You tried to use a variable that was never declared!

###########

try:
    colt
except NameError:
    print("You tried to use a variable that was never declared2!") # You tried to use a variable that was never declared2!

###########

#Any Better?

try:
    colt
except NameError:
    print("You tried to use a variable that was never declared3!") # You tried to use a variable that was never declared3!

print("\n")
###########

def get(d,key):
    try:
        return d[key]
    except KeyError:
        return None

d = {"name": "Ricky"} 
print(get(d, "name")) # Ricky
print(get(d, "city")) # None
print(d["city"])

#   File "d:/MY STUFF/Online courses/Python/FirstProgram/Errors_Handle_Error.py", line 44, in <module>
#    print(d["city"])
# KeyError: 'city'

