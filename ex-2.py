#str = "hel\blo"
#print(str)  # helo
#string = "he said \"ha ha \""
#print(string) # he said "ha ha "

##############
# Set the message variable equal to any string containing a new-line escape sequence
message = "hi\nhere"

# Add a string to the mountains variable that when printed results in: /\/\/\
# You will need to use an escape sequence more than once!
mountains = "/\\/\\/\\"

# Set the quotation variable to any string that contains an escaped double quotation mark

quotation = "he said hi"

message = "Hello \n goodbye"

print(message)  # Hello goodbye
print(quotation)  # he said hi

#############

str_one = "your"
str_two = "face"
str_three = str_one + " " + str_two  
print(str_three)   # your face

##############

username = "bluethecat"
print("Hello there and welcome to the game, " + username)  # Hello there and welcome to the game, bluethecat

#guess = 9
#print("your guess of " + guess + "wrong")  # error message

##############

str_one = "ice"
str_one += " cream"
print(str_one)  # ice cream

##############


name = "colt"
name += " steele"
print(name)  # colt steele

people = 99
people += 1
print(people)  # 100

people -= 10
print(people)  # 90

people *= 10
print(people)  # 900

###############

greeting = "hello"
name = "Heisenberg"
greet_name = greeting + ' ' + name
print(greet_name)  # hello Heisenberg

#Formatting Strings
x = 10
formatted = f"I've told you {x} times already!"
print(formatted)  # I've told you 10 times already!

guess = 8
print(f"your guess of {guess} was incorrect!")  # your guess of 8 was incorrect!

guess = 8
print(f"your guess of {guess + 1} was incorrect!")  # your guess of 9 was incorrect!

x = 10
formatted = "I've told you {} times already!" .format(10)
print(formatted)  # I've told you 10 times already!

fruit = "banana"
ripeness = "unripe"
print(f"The {fruit} is {ripeness}")  # The banana is unripe
print("The {} is {}".format(fruit, ripeness))  # The banana is unripe

##################

first = "Tetiana"
last = "Sobchyshyna"

print("the {} is {}".format(first, last))  # the Tetiana is Sobchyshyna

##################

first = "Venus"
last = "Williams"
formatted = "First Name: {}, Last Name: {}".format(first, last)
print(formatted)  # First Name: Venus, Last Name: Williams

##################
name = "Chuck"
print(name[0])  # C
print(name[1])  # h
print(name[2])  # u
print(name[3])  # C
print(name[4])  # k

answer = "yaaaaaaa"
print(answer[0])  # y
print(answer[-1])  # a

#Converting Data Types

decimal = 12.88769867086
integer = int(decimal)
print(integer)  # 12

###########
#my_list = [1, 2, 3]
#my_list_as_a_string = str(my_list)
#print(my_list_as_a_string)

num = 12
type (num)
num = float(num)
print(num)  # 12.0

num = float(num)
print(type(num))  # <class 'float'>

print(int(99.44423))  # 99

st = str(8)
print(st)  # 8

number = 999
number_as_string = str(number)
print(number_as_string)  # 999

#int = "i am a number"
#print(int)  # i am a number



