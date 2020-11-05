# Ex-44_functions.py
'''return_day'''

'''Write a function called return_day. this function takes in one paramenter
(a number from 1-7 and returns the day of the week (1 is Sunday, 2 is Monday,
3 is Tuesday etc.) If the number is less than 1 or greater that 7, the function
should return None

Hint: store the days of the week in a list (or dict using numbers as keys) '''

'''
return_day(1) # "Sunday"
return_day(2) # "Monday"
return_day(3) # "Tuesday"
return_day(4) # "Wednesday"
return_day(5) # "Thursday"
return_day(6) # "Friday"
return_day(7) # "Saturday"
return_day(41) # None
'''

def return_day(day):
    if day == 1:
        return "Sunday"
    if day == 2:
        return "Monday"  
    if day == 3:
        return "Tuesday"
    if day == 4:
        return "Wednesday"
    if day == 5:
        return "Thursday"
    if day == 6:
        return "Friday"
    if day == 7:
        return "Saturday"
    else:
        return None
print(return_day(1)) # Sunday
print(return_day(4)) # Wednesday

print("\n")
##########

#Here's a solution that uses what we've learned so far.  

#Keep track of the days in a list.  
#Check to make sure num isn't < 0 or  > 6.  
#Return the corresponding day. Use days[num-1] because return_day(1) should return 0th item in list.
def return_day2(num):
    days = ["Sunday","Monday", "Tuesday","Wednesday","Thursday","Friday","Saturday"]
    # Check to see if num valid
    if num > 0 and num <= len(days):
        # use num - 1 because lists start at 0 
        return days[num-1]
    return None

print(return_day2(2)) # Monday
print(return_day2(5)) # Thursday

