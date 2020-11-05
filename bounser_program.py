# ask for age
#age = input("How pld are you: ")
#if age != "":
#    if int(age) >= 18 and int(age) < 21:
#        print("You can enter, but need a wristband!") # 18-21 wristband
#    elif int(age) >= 21:
#        print("You are good to enter and can drink!") # 21 + drink, normal entry
#    else:
#        print("You can't come in, little one! :(")   # too young, sorry
#else:
#    print("Please enter an age!")



# ask for age
age = input("How pld are you: ")
if age:
    age = int(age)
    if age >= 18 and age < 21:
        print("You can enter, but need a wristband!") # 18-21 wristband
    elif age >= 21:
        print("You are good to enter and can drink!") # 21 + drink, normal entry
    else:
        print("You can't come in, little one! :(")   # too young, sorry
else:
    print("Please enter an age!")    


# refactoring
age = input("How pld are you: ")
if age:
    age = int(age)
    if age >= 21:
        print("You can enter, but need a wristband!") # 18-21 wristband
    elif age >= 18:
        print("You are good to enter and can drink!") # 21 + drink, normal entry
    else:
        print("You can't come in, little one! :(")   # too young, sorry
else:
    print("Please enter an age!")  # if the user enters empty spring 