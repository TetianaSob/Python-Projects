# Ex-84_Week_Generator_Exercise.py

'''Write a function called week, which returns a generator that yields
each day of the week, starting with Monday and ending with Sunday.
After Sunday, the generator is exhausted.
It does not start over.'''

'''
days = week()
next(days) # 'Monday'
next(days) # 'Tuesday'
next(days) # 'Wednesday'
next(days) # 'Thursday'
next(days) # 'Friday'
next(days) # 'Saturday'
next(days) # 'Sunday'
next(days) # StopIteration
'''

# def week():
#     pass

'''Week Generator Solution
Define the generator function week  which has a list of days.  
Iterate over the days and yield each day.   
After "Sunday", the generator is exhausted.  
It does not start over.'''

def week():
    days = [
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
        "Sunday"
    ]
    for day in days:
        print(day)

#week()
# Monday
# Tuesday
# Wednesday
# Thursday
# Friday
# Saturday
# Sunday
#print(next(week())) # Monday  
 
print("\n")

# days = week()
# next(days) # 'Monday'
# next(days) # 'Tuesday'


