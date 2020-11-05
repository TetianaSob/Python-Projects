# Ex-49_functions.py
'''list_manipulation'''

'''Write a function called list_manipulation. This function should take in four parameters
(a list,command, location and value)

- If the command in "remove" and the location is "end", the function should 
remove the last value in the list and return the value removed
-If the command is "remove" and the location is "beginning", the function
should remove the first value in the list and return the value removed
- If the command is "add" and the location is "end", the function should add the
value (fourth parameter) to the end og the list and return the list. '''

'''
list_manipulation([1,2,3], "remove", "end") # 3
list_manipulation([1,2,3], "remove", "beginning") #  1
list_manipulation([1,2,3], "add", "beginning", 20) #  [20,1,2,3]
list_manipulation([1,2,3], "add", "end", 30) #  [1,2,3,30]
'''

def list_manipulation(collection, command, location, value=None):
    if(command == "remove" and location == "end"):
        return collection.pop()
    elif(command == "remove" and location == "beginning"):
        return collection.pop(0)
    elif(command == "add" and location == "beginning"):
        collection.insert(0,value)
        return collection
    elif(command == "add" and location == "end"):
        collection.append(value)
        return collection

print(list_manipulation([1,2,3], "remove", "end")) # 3
print(list_manipulation([1,2,3], "remove", "beginning")) # 1
print(list_manipulation([1,2,3], "add", "beginning", 20)) #  [20, 1, 2, 3]
print(list_manipulation([1,2,3], "add", "end", 30)) # [1, 2, 3, 30]