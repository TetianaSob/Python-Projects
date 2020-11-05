countries = ['Argentina', 'Gutemala', 'Russia', 'Yemen']
print(countries.pop()) # Yemen
print(countries) # ['Argentina', 'Gutemala', 'Russia']

#########

def add(a,b):
    return a+b

print(add(1,4)) # 5
 
print("\n")
##########

def add(a=10, b=20):
    return a+b

print(add(1,7)) #8
