# Ex-101_find_user.py

'''For this exercise, you'll be working with files called 'users.csv'. Each 
row of data consists of two columns: a user's name, and a user's last name.

Implement the following function:
'find_user': Takes in a first name and the last name and searches for a
user with first and last name in the 'users.csv' file. If the user is found,
'find_user' returns the index where the user is found. Otherwise it returns
a massage stating that the user wasn't found.
'''
'''
find_user("Colt", "Steele") # 1
find_user("Alan", "Turing") # 3
find_user("Not", "Here") # 'Not Here not found.'
'''

#Find User CSV Solution
import csv
 
def find_user(first_name, last_name):
    with open("users.csv") as csvfile:
        csv_reader = csv.reader(csvfile)
        for (index, row) in enumerate(csv_reader):
            first_name_match = first_name == row[0]
            last_name_match = last_name == row[1]
            if first_name_match and last_name_match:
                return index
        return "{} {} not found.".format(first_name, last_name)

print(find_user("Colt", "Steele")) # 2
print(find_user("Dwayne", "Johnson")) # 1
print(find_user("Alan", "Turing")) # Alan Turing not found.

# users.csv file
# first_name	last_name
# Dwayne	Johnson
# Colt	Steele

