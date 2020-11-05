# Decorators3_Preserving_Metadata.py

def log_function_data(fn):
    def wrapper(*args, **kwargs):
        print(f"you are about to call {fn.__name__}")
        print(f"Here's the documentation: {fn.__doc__}")
        return fn(*args, **kwargs)
    return wrapper

@log_function_data
def add(x,y):
    '''Adds two numbers together.'''
    return x + y

print(add(10,30))  # 40   

print(add.__doc__) # None
print(add.__name__) # wrapper
print(help(add))
# Help on function wrapper in module __main__:
# wrapper(*args, **kwargs)