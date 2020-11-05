# ex-39.py

#Define a function called generate_evens
#It should return a list of even numbers between 1 and 50(not including 50)
def generate_evens():
    number = 2
    if number % 2 == 0:
        return "even"
    else:
        return "odd"
    
print(generate_evens()) # even

print("\n")
############

# Generating evens using a list comprehension:
def generate_evens():
    return [x for x in range(1,50) if x%2 == 0]
#Generating evens using a loop:

def generate_evens():
    result = []
    for x in range(1,50):
        if x % 2 == 0:
            result.append(x)
    return result # even