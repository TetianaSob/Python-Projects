friends = ['ashley', 'matt', 'michael']
 
[friend[0].upper() for friend in friends] # ['Ashley', 'Matt', 'Michael']
print(friends) # ['ashley', 'matt', 'michael']

########### 
print("\n")

friends2 = ['ashley', 'matt', 'michael']
 
print([friend[0].upper() + friend[1:] for friend in friends]) # this actually returns ['Ashley', 'Matt', 'Michael']
# ['Ashley', 'Matt', 'Michael']

##########
print("\n")

friends3 = ['ashley', 'matt', 'michael']
 
print([friend.capitalize() for friend in friends])
# ['Ashley', 'Matt', 'Michael']