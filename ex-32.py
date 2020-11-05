list1 = ["CA", "NJ", "RI"]
list2 = ["California", "New Jersey", "Rhode Island"]

# make sure your solution is assigned to the answer variable so the tests can work!
answer = {list1[i]: list2[i] for i in range(0, len(list1))}

print(answer) # {'CA': 'California', 'NJ': 'New Jersey', 'RI': 'Rhode Island'}

print("\n")
#######

list1 = ["CA", "NJ", "RI"]
list2 = ["California", "New Jersey", "Rhode Island"]
 
answer2 = {list1[i]: list2[i] for i in range(0,3)}

print(answer2) # {'CA': 'California', 'NJ': 'New Jersey', 'RI': 'Rhode Island'}

print("\n") 
#######

list1 = ["CA", "NJ", "RI"]
list2 = ["California", "New Jersey", "Rhode Island"]
 
print(dict(zip(list1,list2))) # {'CA': 'California', 'NJ': 'New Jersey', 'RI': 'Rhode Island'}