# High_Order_Functions.py

def sum(n, func):
    total  = 0
    for num in range(1, n+1):
        total += func(num)
    return total

def square(x):
    return x*x

def cube(x):
    return x*x*x

print(sum(10, square)) # 385
print(sum(5, square)) # 55

print(sum(3, cube)) # 36