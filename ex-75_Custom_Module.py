# ex-75_Custom_Module.py

'''Your task is to write a function in the "helpers.py", and then call
it from the "ecercise.py" file. More specifically:'''

#Import your helpers module here.  Do not use the 'from' or 'as' syntax, 
# just use a plain old 'import'

#Call the lucky_number function from your helpers module, and save 
# the result to a variable called num

'''Custom Module Exercise
This exercise tested your ability to write simple code in one file and import it into another file.

In helpers.py:
I started by defining lucky_number  in helpers.py :
'''

def lucky_number():
    return 37

'''
In exercise.py:
I import my helpers module first.  And then I call helpers.lucky_number()  and save the result to the num  variable

#Import your helpers module here.  Do not use the 'from' or 'as' syntax, just use a plain old 'import'
import helpers
 
 
#Call the lucky_number function from your helpers module, and save the result to a variable called num
'''
num = helpers.lucky_number()
