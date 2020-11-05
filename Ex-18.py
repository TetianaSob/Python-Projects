#A solution using append()

# Create a list called instructors
instructors = []
# Add the following strings to the instructors list 
    # "Colt"
    # "Blue"
    # "Lisa"
 
instructors.append("Colt")
instructors.append("Blue")
instructors.append("Lisa")

print(instructors)  # ['Colt', 'Blue', 'Lisa']
print("\n")
###########

#A solution using extend()

# Create a list called instructors
instructors = []
# Add the following strings to the instructors list 
    # "Colt"
    # "Blue"
    # "Lisa"
# Use any of the list methods we've seen to accomplish this:
instructors.extend(["Colt", "Blue", "Lisa"])

print(instructors) # ['Colt', 'Blue', 'Lisa']