# Errors_Try_Except_Finally.py
'''
try:
    num = int(input("please enter a number: "))
except:
    print("That's not a number") # please enter a number: 1

#please enter a number: et
#That's not a number
'''

'''
try:
    num = int(input("please enter a number: "))
except:
    print("That's not a number") # please enter a number: 1
else:
    print("I'M IN THE ELSE!") # I'M IN THE ELSE!
finally:
    print("RUNS No MATTER WHAT")

# please enter a number: 2
# I'M IN THE ELSE!
# RUNS No MATTER WHAT
'''

while True:
    try:
        num = int(input("please enter a number: "))
    except ValueError:
        print("That's not a number") # please enter a number: 1
    else:
        print("Good job, you entered a number!") # I'M IN THE ELSE!
        break
    finally:
        print("RUNS No MATTER WHAT") 
print("REST OF GAME LOGIC RUNS")

# please enter a number: qw
# That's not a number
# RUNS No MATTER WHAT

# please enter a number: 5
# Good job, you entered a number!
# RUNS No MATTER WHAT
# REST OF GAME LOGIC RUNS