# guessing game

# import random

# random_number = random.randint(1,10)
# print(random_number)

# 5
# 10

######

# import random

# random_number = random.randint(1,10)
# guess = input("Pick a number from 1 to 10: ")
# guess = int(guess)

# if guess == random_number:
#     print("YOU GOT IT!")
# elif guess < random_number:
#     print("TOO LOW!")
# else:
#     print("TOO HIGH!")

# print(random_number)

# Pick a number from 1 to 10: 3
# TOO HIGH!
# 2

###########

import random

random_number = random.randint(1,10)
guess = None

while True:
    guess = input("Pick a number from 1 to 10: ")
    guess = int(guess)
    if guess < random_number:
        print("TOO LOW!")
    elif guess > random_number:
        print("TOO HIGH!")
    else:
        print("YOU WON!!!")
        play_again = input("Do you want to play again? (y/n) ")
        if play_again == "y":
            random_number = random.randint(1, 10)
            guess = None
        else:
            print("Thank you for playing!")
            break

print(random_number)

# Pick a number from 1 to 10: 7
# TOO LOW!
# Pick a number from 1 to 10: 10
# TOO HIGH!
# Pick a number from 1 to 10: 8
# TOO LOW!
# Pick a number from 1 to 10: 9
# YOU WON!!!