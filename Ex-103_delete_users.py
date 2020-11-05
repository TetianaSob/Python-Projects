# Ex-103_delete_users.py
'''For this exercise, you'll be working with a file called 'users.csv'.
Each row of data consists of two columns: a user's first name and user's
last name.
Implement the following function:
'delete_users': Takes is a first name and a last name. Updates the 'users.csv'
file so that ant user whose first and last names match the inputs are removed.
The function should return a count of how many users were removed.
'''

'''
delete_users("Grace", "Hopper") # Users deleted: 1.
delete_users("Colt", "Steele") # Users deleted: 2.
delete_users("Not", "Here") # Users deleted: 0.
'''

#Delete Users CSV Solution
import csv
 
def delete_users(first_name, last_name):
    with open("users.csv") as csvfile:
        csv_reader = csv.reader(csvfile)
        rows = list(csv_reader)
 
    count = 0
    with open("users.csv", "w") as csvfile:
        csv_writer = csv.writer(csvfile)
        for row in rows:
            if row[0] == first_name and row[1] == last_name:
                count += 1
            else:
                csv_writer.writerow(row)
 
    return "Users deleted: {}.".format(count)

#delete_users("Grace", "Hopper")
delete_users("2", "2")

# first_first	last_last
	
# 1	1
	
# 3	3
	
# 4	4
	
# 5	5
