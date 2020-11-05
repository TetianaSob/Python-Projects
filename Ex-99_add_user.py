# Ex-99_add_user.py

''' For this exercise, you'll be working with file called 'users.csv'. 
Eacg row of a data consists of two user's first name, and user's last name.

Implement the following function:
'add_user': Takes is a first name and a last name and adds a new user to the 
'users.csv' file.
'''

'''
add_user("Dwayne", "Johnson") # None
# CSV now has two data rows:

# First Name,Last Name
# Colt,Steele
# Dwayne,Johnson
'''

#Add User CSV Solution
import csv
 
def add_user(first_name, last_name):
    with open("users.csv", "a") as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow([first_name, last_name])

add_user("Dwayne", "Johnson")        