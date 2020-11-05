# for loops
for number in range(1, 8):
    print(number)
#1
#2
#3
#4
#5
#6
#7

for x in range (1, 10):
    print(x)
    print(x * x)
#1
#1
#2
#4
#3
#9
#4
#16
#5
#25
#6
#36
#7
#49
#8
#64
#9
#81

#####
for letter in "coffee":
    print(letter)

#c
#o
#f
#f
#e
#e    

print(list(range(10))) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(list(range(1, 8))) # [1, 2, 3, 4, 5, 6, 7]
print(list(range(1, 10, 2)))  # [1, 3, 5, 7, 9]
print(list(range(7, 0, -1))) # [7, 6, 5, 4, 3, 2, 1]

r = range(10)
print(r) # range(0, 10)

for num in range(10, 20, 2):
    print(num) 
    
#10
#12
#14
#16
#18

for num in range(100, 20, -10):
    print(num) 

#100
#90
#80
#70
#60
#50
#40
#30   


#What is printed out after the following code?

nums = range(1,5)
print(nums) # range(1, 5)

##########

# Add up all odd numbers between 10 and 20
# Store the result in x:
x = 0

# YOUR CODE GOES HERE:
for n in range (11, 20, 2):
    print(n)
#11
#13
#15
#17
#19

# Add up all odd numbers between 10 and 20
# Store the result in x:
x = 0
 
 
# YOUR CODE GOES HERE:
for n in range(10, 21):  #remember range is exclusive, so we have to go up to 21
    if n % 2 != 0:
        x += n
        print(n)

#11
#13
#15
#17
#19       

##########
print("Program repeat")

#times = input("How many times do I need to tell you? ")
#times = int(times)

for time in range(5):
    print(f"time {time} CLEAN UP YOUR ROOM")

#Program repeat
#time 0 CLEAN UP YOUR ROOM
#time 1 CLEAN UP YOUR ROOM
#time 2 CLEAN UP YOUR ROOM
#time 3 CLEAN UP YOUR ROOM
#time 4 CLEAN UP YOUR ROOM  
