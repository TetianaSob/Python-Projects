# Decorators3_Syntax.py

def be_polite(fn):
    def wrapper():
        print("What a pleasure to meet you!")
        fn()
        print("Have a great day!")
    return wrapper

@be_polite
def greet():
    print("My name is Matt.")

@be_polite
def rage():
    print("I HATE YOU!")


#greet = be_polite(greet)  # because @be_polite is called we don't need to call it any more 
#rage = be_polite(rage)

print(greet()) 
# What a pleasure to meet you!
# My name is Matt.
# Have a great day!
# None
print("\n")

print(rage())
# What a pleasure to meet you!
# I HATE YOU!
# Have a great day!
# None


