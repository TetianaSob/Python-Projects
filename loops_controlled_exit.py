#Controled exit

# while True:
#     command = input("Type 'exit' to exit: ")
#     if (command == "exit"):
#         break

for x in range(1, 101):
    print(x)
    if x == 3:
        break

# 1
# 2
# 3

######### Adding a break

times = int(input("How many times do I have to tell you? "))

for time in range (times):
    print("CLEAN UP YOUR ROOM!")
    if time >= 4:
        print("do you even listen anymore?")
        break

# How many times do I have to tell you? 2
# CLEAN UP YOUR ROOM!
# CLEAN UP YOUR ROOM!    