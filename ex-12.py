# NO TOUCHING ======================================
from random import choice, randint
 
actually_sick = choice([True, False])
kinda_sick = choice([True, False])
hate_your_job = choice([True, False])
sick_days = randint(0, 10)
# NO TOUCHING ======================================
 
 
calling_in_sick = None  # set this to True or False with Boolean Logic and Conditionals!
 
# Note, we don't need to check if actually_sick == True
#  Instead, just check if actually_sick, since it's a boolean
 
if actually_sick and sick_days > 0:
    calling_in_sick = True
elif kinda_sick and hate_your_job and sick_days > 0:
    calling_in_sick = True
else:
    calling_in_sick = False
    
