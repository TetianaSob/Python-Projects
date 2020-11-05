# function_kwargs.py

''' A special operator we can pass to function

Gathers remaining keyword arguments as a dictionary

This is just s parameter - you can call it whatever you want!'''

def fav_colors(**kwargs):
    print(kwargs)

fav_colors(colt="purple", ruby= "red", ethel = "teal") # {'colt': 'purple', 'ruby': 'red', 'ethel': 'teal

print("\n")
#############

def fav_colors(**kwargs):
    for person, color in kwargs.items():
        print(f"{person}'s favourite color is  {color}")
    
fav_colors(colt="purple", ruby= "red", ethel = "teal") 
# colt's favourite color is  purple
#ruby's favourite color is  red
#ethel's favourite color is  teal

print("\n")

fav_colors(colt="purple", ruby= "red", ethel = "teal") 
fav_colors(colt="purple", ruby= "red", ethel = "teal", ted = "blue") 
fav_colors(colt="royal deep amazing purple") 

# colt's favourite color is  purple
# ruby's favourite color is  red
# ethel's favourite color is  teal
# colt's favourite color is  purple
# ruby's favourite color is  red
# ethel's favourite color is  teal
# ted's favourite color is  blue
# colt's favourite color is  royal deep amazing purple

print("\n")
###########

def special_greeting(**kwargs):
    if "David" in kwargs and kwargs["David"] == "special":
        return "You get a special greeting David!"
    elif "David" in kwargs:
        return f"{kwargs['David']} David!"
    
    return "Not sure who this is..."

print(special_greeting(David='Hello')) # Hello David!
print(special_greeting(Bob='hello')) # Not sure who this is...
print(special_greeting(David='special')) # You get a special greeting David!

print(special_greeting(Heather="hello", David="special")) # You get a special greeting David!