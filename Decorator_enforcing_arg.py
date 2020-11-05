# Decorator_enforcing_arg.py

def enforce(*types):
    def decorator(f):
        def new_func(*args, **kwargs):
            newargs = []
            for (a, t) in zip(args, types):
                newargs.append(t(a))
            return f(*newargs, **kwargs)
        return new_func
    return decorator

@enforce(str, int)
def repeat_msg(msg, times):
    for time in range(times):
        print(msg)

@enforce(float, float)
def divide(a,b):
    return a/b

@enforce(float, float)
def multiple(a,b):
    return a*b

@enforce(float, float)
def cube(a,b):
    return a**3   

print(repeat_msg("hello", '3'))
# hello
# hello
# hello
print("\n")

print(repeat_msg("hi", '5'))
# hi
# hi
# hi
# hi
# hi
# ("hello", str) ('3', int)
# ["hello", 3]
print("\n")

print(divide(5, 5)) # 1.0
print(divide(15, 5)) # 3.0

print("\n")
print(multiple(5, 5)) # 25.0

print("\n")
print(cube(5, 5)) # 125.0